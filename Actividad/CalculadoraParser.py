# Generated from Calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,9,2,1,
        3,1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,3,4,39,8,4,1,5,
        1,5,1,5,3,5,44,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,56,
        8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,1,2,1,0,3,4,56,0,14,1,0,0,
        0,2,17,1,0,0,0,4,19,1,0,0,0,6,27,1,0,0,0,8,35,1,0,0,0,10,43,1,0,
        0,0,12,55,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,
        3,4,2,0,18,3,1,0,0,0,19,24,3,6,3,0,20,21,7,0,0,0,21,23,3,6,3,0,22,
        20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,5,1,0,0,
        0,26,24,1,0,0,0,27,32,3,8,4,0,28,29,7,1,0,0,29,31,3,8,4,0,30,28,
        1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,7,1,0,0,0,34,
        32,1,0,0,0,35,38,3,10,5,0,36,37,5,5,0,0,37,39,3,8,4,0,38,36,1,0,
        0,0,38,39,1,0,0,0,39,9,1,0,0,0,40,41,5,2,0,0,41,44,3,10,5,0,42,44,
        3,12,6,0,43,40,1,0,0,0,43,42,1,0,0,0,44,11,1,0,0,0,45,46,5,9,0,0,
        46,47,5,6,0,0,47,48,3,2,1,0,48,49,5,7,0,0,49,56,1,0,0,0,50,51,5,
        6,0,0,51,52,3,2,1,0,52,53,5,7,0,0,53,56,1,0,0,0,54,56,5,8,0,0,55,
        45,1,0,0,0,55,50,1,0,0,0,55,54,1,0,0,0,56,13,1,0,0,0,5,24,32,38,
        43,55
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "FUNC_NAME", "WS" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_addExpr = 2
    RULE_multExpr = 3
    RULE_powExpr = 4
    RULE_unaryExpr = 5
    RULE_primary = 6

    ruleNames =  [ "prog", "expresion", "addExpr", "multExpr", "powExpr", 
                   "unaryExpr", "primary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    FUNC_NAME=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expresion()
            self.state = 15
            self.match(CalculadoraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self):
            return self.getTypedRuleContext(CalculadoraParser.AddExprContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.addExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.MultExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.MultExprContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_addExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)




    def addExpr(self):

        localctx = CalculadoraParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.multExpr()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.multExpr()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.PowExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.PowExprContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_multExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)




    def multExpr(self):

        localctx = CalculadoraParser.MultExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_multExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.powExpr()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.powExpr()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(CalculadoraParser.UnaryExprContext,0)


        def powExpr(self):
            return self.getTypedRuleContext(CalculadoraParser.PowExprContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_powExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpr" ):
                listener.enterPowExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpr" ):
                listener.exitPowExpr(self)




    def powExpr(self):

        localctx = CalculadoraParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_powExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.unaryExpr()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 36
                self.match(CalculadoraParser.T__4)
                self.state = 37
                self.powExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_unaryExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NegacionContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryExpr(self):
            return self.getTypedRuleContext(CalculadoraParser.UnaryExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacion" ):
                listener.enterNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacion" ):
                listener.exitNegacion(self)


    class PositivoContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(CalculadoraParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositivo" ):
                listener.enterPositivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositivo" ):
                listener.exitPositivo(self)



    def unaryExpr(self):

        localctx = CalculadoraParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryExpr)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = CalculadoraParser.NegacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(CalculadoraParser.T__1)
                self.state = 41
                self.unaryExpr()
                pass
            elif token in [6, 8, 9]:
                localctx = CalculadoraParser.PositivoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class FuncionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC_NAME(self):
            return self.getToken(CalculadoraParser.FUNC_NAME, 0)
        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)


    class ParentesisContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)



    def primary(self):

        localctx = CalculadoraParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = CalculadoraParser.FuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(CalculadoraParser.FUNC_NAME)
                self.state = 46
                self.match(CalculadoraParser.T__5)
                self.state = 47
                self.expresion()
                self.state = 48
                self.match(CalculadoraParser.T__6)
                pass
            elif token in [6]:
                localctx = CalculadoraParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(CalculadoraParser.T__5)
                self.state = 51
                self.expresion()
                self.state = 52
                self.match(CalculadoraParser.T__6)
                pass
            elif token in [8]:
                localctx = CalculadoraParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(CalculadoraParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





