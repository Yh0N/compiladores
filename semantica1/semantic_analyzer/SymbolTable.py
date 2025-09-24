# semantic_analyzer/SymbolTable.py

class Symbol:
    def __init__(self, name: str, typ: str):
        self.name = name
        self.type = typ  # "int" | "string"

    def __repr__(self):
        return f"<Var {self.type} {self.name}>"


class SymbolTable:
    """
    Tabla de símbolos con pila de ámbitos.
    - Cada ámbito es un dict: nombre -> Symbol
    - El último elemento de scope_stack es el ámbito actual.
    """
    def __init__(self):
        self.scope_stack = [{}]  # ámbito global

    # ----- Ámbitos -----
    def enter_scope(self) -> None:
        """Crea un nuevo ámbito (por ejemplo al entrar a un bloque '{')."""
        self.scope_stack.append({})

    def exit_scope(self) -> None:
        """Sale del ámbito actual (por ejemplo al cerrar un bloque '}')."""
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()

    # ----- Consultas -----
    def lookup(self, name: str):
        """Busca un símbolo desde el ámbito actual hacia el global."""
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None

    def in_current_scope(self, name: str) -> bool:
        """¿Existe el nombre en el ámbito actual?"""
        return name in self.scope_stack[-1]

    # ----- Inserción -----
    def insert(self, name: str, symbol: Symbol) -> bool:
        """
        Inserta un símbolo en el ámbito actual.
        Devuelve False si el nombre ya existe en ese mismo ámbito (redeclaración).
        """
        current_scope = self.scope_stack[-1]
        if name in current_scope:
            return False
        current_scope[name] = symbol
        return True

    # Azúcar: declarar variable rápidamente
    def declare(self, name: str, typ: str) -> bool:
        return self.insert(name, Symbol(name, typ))