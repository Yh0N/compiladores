# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#expresion.
    def enterExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expresion.
    def exitExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#addExpr.
    def enterAddExpr(self, ctx:CalculadoraParser.AddExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#addExpr.
    def exitAddExpr(self, ctx:CalculadoraParser.AddExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#multExpr.
    def enterMultExpr(self, ctx:CalculadoraParser.MultExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#multExpr.
    def exitMultExpr(self, ctx:CalculadoraParser.MultExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#powExpr.
    def enterPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#powExpr.
    def exitPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Negacion.
    def enterNegacion(self, ctx:CalculadoraParser.NegacionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Negacion.
    def exitNegacion(self, ctx:CalculadoraParser.NegacionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Positivo.
    def enterPositivo(self, ctx:CalculadoraParser.PositivoContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Positivo.
    def exitPositivo(self, ctx:CalculadoraParser.PositivoContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Funcion.
    def enterFuncion(self, ctx:CalculadoraParser.FuncionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Funcion.
    def exitFuncion(self, ctx:CalculadoraParser.FuncionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parentesis.
    def enterParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parentesis.
    def exitParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Numero.
    def enterNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Numero.
    def exitNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass



del CalculadoraParser