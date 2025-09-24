# semantic_analyzer/SemanticVisitor.py
from antlr4 import *
from antlr4.Token import CommonToken
from generated.WhileLangVisitor import WhileLangVisitor
from generated.WhileLangParser import WhileLangParser
from .SymbolTable import SymbolTable, Symbol

INT_T  = "int"
STR_T  = "string"
BOOL_T = "bool"
ERR_T  = "error"

class WhileSemantic(WhileLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.errors = []
        self.in_while = 0  # profundidad de while anidado

    # ---------------- utilidades ----------------
    def error(self, ctx, msg: str):
        tok = ctx.start if hasattr(ctx, "start") else None
        where = f"[line {tok.line}, col {tok.column}] " if isinstance(tok, CommonToken) else ""
        self.errors.append(where + msg)

    # Tipado de op aritméticos
    def _bin_arith(self, op: str, t1: str, t2: str, ctx) -> str:
        if op == '+':
            if t1 == INT_T and t2 == INT_T: return INT_T
            if t1 == STR_T and t2 == STR_T: return STR_T
            if t1 != ERR_T and t2 != ERR_T:
                self.error(ctx, f"Operación '+' inválida para {t1} + {t2}")
            return ERR_T
        # '-', '*', '/'
        if t1 == INT_T and t2 == INT_T: return INT_T
        if t1 != ERR_T and t2 != ERR_T:
            self.error(ctx, f"Operación '{op}' requiere int,int (recibido {t1},{t2})")
        return ERR_T

    # Tipado de comparaciones (condition usa operator explícito)
    def _bin_cmp(self, op: str, t1: str, t2: str, ctx) -> str:
        if op in ('>', '<'):
            if t1 == INT_T and t2 == INT_T: return BOOL_T
            self.error(ctx, f"Comparación '{op}' requiere int,int (recibido {t1},{t2})")
            return ERR_T
        if op in ('==', '!='):
            if t1 == t2 and t1 in (INT_T, STR_T): return BOOL_T
            self.error(ctx, f"Comparación '{op}' requiere tipos iguales compatibles (recibido {t1},{t2})")
            return ERR_T
        return ERR_T

    # ---------------- programa ----------------
    def visitProgram(self, ctx: WhileLangParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)
        return self.errors

    # ---------------- declaraciones ----------------
    # declaration : type ID ASSIGN expr SEMI | type ID SEMI ;
    def visitDeclaration(self, ctx: WhileLangParser.DeclarationContext):
        typ = ctx.type_().getText()  # nota: regla 'type' -> método type_() en ANTLR Python
        name = ctx.ID().getText()

        if not self.table.insert(name, Symbol(name, typ)):
            self.error(ctx, f"Redeclaración en el mismo ámbito: '{name}'")

        # Si tiene inicialización
        if ctx.expr():
            rt = self.visit(ctx.expr())
            if rt != ERR_T and rt != typ:
                self.error(ctx, f"Incompatibilidad en inicialización: {typ} {name} = {rt}")
        return None

    # ---------------- asignación ----------------
    # assignment : ID ASSIGN expr SEMI ;
    def visitAssignment(self, ctx: WhileLangParser.AssignmentContext):
        name = ctx.ID().getText()
        sym = self.table.lookup(name)
        if sym is None:
            self.error(ctx, f"Variable no declarada: '{name}'")
            _ = self.visit(ctx.expr())  # seguir analizando RHS
            return None
        rt = self.visit(ctx.expr())
        if rt != ERR_T and sym.type != rt:
            self.error(ctx, f"Asignación incompatible: {sym.type} {name} = {rt}")
        return None

    # ---------------- while ----------------
    # whileStatement : WHILE LPAREN condition RPAREN LBRACE statement* RBRACE ;
    def visitWhileStatement(self, ctx: WhileLangParser.WhileStatementContext):
        ctype = self.visit(ctx.condition())
        if ctype != BOOL_T and ctype != ERR_T:
            self.error(ctx, f"La condición del while debe ser booleana, recibido {ctype}")
        self.in_while += 1
        # abrir scope de bloque
        self.table.enter_scope()
        for st in ctx.statement():
            self.visit(st)
        self.table.exit_scope()
        self.in_while -= 1
        return None

    # ---------------- if ----------------
    # ifStatement : IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)? ;
    def visitIfStatement(self, ctx: WhileLangParser.IfStatementContext):
        ctype = self.visit(ctx.condition())
        if ctype != BOOL_T and ctype != ERR_T:
            self.error(ctx, f"La condición del if debe ser booleana, recibido {ctype}")

        # THEN block: primeros K statements hasta la primera RBRACE
        then_stmts, else_stmts = self._partition_if_statements(ctx)

        self.table.enter_scope()
        for st in then_stmts:
            self.visit(st)
        self.table.exit_scope()

        if else_stmts:
            self.table.enter_scope()
            for st in else_stmts:
                self.visit(st)
            self.table.exit_scope()

        return None

    def _partition_if_statements(self, ctx: WhileLangParser.IfStatementContext):
        """
        Divide ctx.statement() en (then_stmts, else_stmts) escaneando los hijos
        y contando qué statements quedan entre las llaves del THEN y del ELSE.
        """
        all_stmts = list(ctx.statement())
        then_stmts = []
        else_stmts = []

        # escaneo de hijos para separar por llaves
        children = list(ctx.getChildren())
        i = 0
        # Buscar bloque THEN: después de RPAREN debe venir LBRACE
        # Contar cuántos StatementContext hay entre esa LBRACE y su RBRACE emparejada
        # Luego, si hay ELSE, repetir para ELSE.
        # Usamos un índice sobre all_stmts para repartirlos en orden.
        stmt_index = 0

        # Encontrar primera LBRACE (then)
        # luego contar RBRACE con profundidad 1
        depth = 0
        in_then = False
        in_else = False

        while i < len(children):
            ch = children[i]
            text = getattr(ch, "getText", lambda: "")()
            # Enter THEN block
            if not in_then and text == '{':
                in_then = True
                depth = 1
                i += 1
                continue

            if in_then:
                if isinstance(ch, WhileLangParser.StatementContext):
                    then_stmts.append(all_stmts[stmt_index]); stmt_index += 1
                elif text == '{':
                    depth += 1
                elif text == '}':
                    depth -= 1
                    if depth == 0:
                        in_then = False
                        # Puede venir ELSE...
                i += 1
                continue

            # ELSE token activa bloque else
            if not in_else and text == 'else':
                # la siguiente '{' abre else
                in_else = True
                # avanzar hasta la '{'
                i += 1
                while i < len(children) and getattr(children[i], "getText", lambda: "")() != '{':
                    i += 1
                depth = 1
                i += 1
                continue

            if in_else:
                if i >= len(children): break
                ch = children[i]
                text = getattr(ch, "getText", lambda: "")()
                if isinstance(ch, WhileLangParser.StatementContext):
                    else_stmts.append(all_stmts[stmt_index]); stmt_index += 1
                elif text == '{':
                    depth += 1
                elif text == '}':
                    depth -= 1
                    if depth == 0:
                        in_else = False
                        break
                i += 1
                continue

            i += 1

        return then_stmts, else_stmts

    # ---------------- break / continue ----------------
    def visitBreakStatement(self, ctx: WhileLangParser.BreakStatementContext):
        if self.in_while == 0:
            self.error(ctx, "break fuera de while")
        return None

    def visitContinueStatement(self, ctx: WhileLangParser.ContinueStatementContext):
        if self.in_while == 0:
            self.error(ctx, "continue fuera de while")
        return None

    # ---------------- condition ----------------
    # AHORA: condition : expr (operator expr)? ;
    def visitCondition(self, ctx: WhileLangParser.ConditionContext):
        # Si hay operador, es comparación -> debe producir bool si tipos compatibles
        if ctx.operator() is not None:
            t1 = self.visit(ctx.expr(0))
            t2 = self.visit(ctx.expr(1))
            op = ctx.operator().getText()
            return self._bin_cmp(op, t1, t2, ctx)
        else:
            # Solo una expr: parsea, pero no es booleana -> error semántico
            t = self.visit(ctx.expr(0))
            if t != ERR_T:
                self.error(ctx, f"Condición no booleana: se obtuvo '{t}'. Usa comparadores (==, !=, <, <=, >, >=).")
            return ERR_T

    # ---------------- expr ----------------
    # expr : ID | NUMBER | STRING | expr (PLUS|MINUS|MULT|DIV) expr ;
    def visitExpr(self, ctx: WhileLangParser.ExprContext):
        n = ctx.getChildCount()
        if n == 1:
            # átomo: ID | NUMBER | STRING
            child = ctx.getChild(0)
            text = child.getText()

            # Terminal types: try to detect NUMBER / STRING by token type name
            sym = None
            if hasattr(child, "symbol"):
                ttype = child.symbol.type
                # Sin acceso directo a symbolicNames; usamos el texto:
                if text.startswith('"') and text.endswith('"'):
                    return STR_T
                if text.isdigit():
                    return INT_T

            # Si es ID, validamos declaración
            sym = self.table.lookup(text)
            if sym is None:
                # Si no parece literal, lo tratamos como ID no declarado
                if not (text.startswith('"') and text.endswith('"')) and not text.isdigit():
                    self.error(ctx, f"Variable no declarada: '{text}'")
                    return ERR_T
            return sym.type if sym else (STR_T if text.startswith('"') else INT_T)

        elif n == 3:
            # expr op expr
            t1 = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            t2 = self.visit(ctx.expr(1))
            return self._bin_arith(op, t1, t2, ctx)

        # Forma inesperada
        return ERR_T