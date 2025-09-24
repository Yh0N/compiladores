from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 

from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser
from semantic_analyzer.SemanticVisitor import WhileSemantic

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lanza una excepción para detener la ejecución de inmediato
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    try:
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = WhileLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())

        stream = CommonTokenStream(lexer)
        parser = WhileLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        print("Análisis sintáctico completado sin errores.")

        visitor = WhileSemantic() 
        visitor.visit(tree)

        if visitor.errors:
            print("== ERRORES SEMÁNTICOS ==")
            for e in visitor.errors:
                print("-", e)
        else:
            print("Análisis semántico completado sin errores.") 

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()