# Generated from STL.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4H\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5S\n\5\3\5\3\5\3\5\7\5X\n\5\f\5\16\5[\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\2\3\b\7\2\4\6\b\n\2\7\3")
        buf.write("\2\23\24\3\2\30\34\3\2\r\16\3\2\3\4\3\2\17\22\2k\2\r\3")
        buf.write("\2\2\2\4\32\3\2\2\2\6G\3\2\2\2\bR\3\2\2\2\n\\\3\2\2\2")
        buf.write("\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17")
        buf.write("\20\3\2\2\2\20\3\3\2\2\2\21\22\5\6\4\2\22\23\7\37\2\2")
        buf.write("\23\33\3\2\2\2\24\25\7\3\2\2\25\26\7\26\2\2\26\27\5\b")
        buf.write("\5\2\27\30\7\37\2\2\30\33\3\2\2\2\31\33\7\37\2\2\32\21")
        buf.write("\3\2\2\2\32\24\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\35")
        buf.write("\7\5\2\2\35\36\5\6\4\2\36\37\7\6\2\2\37 \t\2\2\2 !\7\5")
        buf.write("\2\2!\"\5\6\4\2\"#\7\6\2\2#H\3\2\2\2$%\7\25\2\2%&\7\5")
        buf.write("\2\2&\'\5\6\4\2\'(\7\6\2\2(H\3\2\2\2)*\5\b\5\2*+\t\3\2")
        buf.write("\2+,\5\b\5\2,H\3\2\2\2-.\7\5\2\2./\5\6\4\2/\60\7\6\2\2")
        buf.write("\60H\3\2\2\2\61H\t\4\2\2\62\63\7\5\2\2\63\64\5\6\4\2\64")
        buf.write("\65\7\6\2\2\65\66\7\n\2\2\66\67\5\n\6\2\678\7\5\2\289")
        buf.write("\5\6\4\29:\7\6\2\2:H\3\2\2\2;<\7\13\2\2<=\5\n\6\2=>\7")
        buf.write("\5\2\2>?\5\6\4\2?@\7\6\2\2@H\3\2\2\2AB\7\f\2\2BC\5\n\6")
        buf.write("\2CD\7\5\2\2DE\5\6\4\2EF\7\6\2\2FH\3\2\2\2G\34\3\2\2\2")
        buf.write("G$\3\2\2\2G)\3\2\2\2G-\3\2\2\2G\61\3\2\2\2G\62\3\2\2\2")
        buf.write("G;\3\2\2\2GA\3\2\2\2H\7\3\2\2\2IJ\b\5\1\2JS\7\35\2\2K")
        buf.write("L\7\20\2\2LS\7\35\2\2MS\t\5\2\2NO\7\5\2\2OP\5\b\5\2PQ")
        buf.write("\7\6\2\2QS\3\2\2\2RI\3\2\2\2RK\3\2\2\2RM\3\2\2\2RN\3\2")
        buf.write("\2\2SY\3\2\2\2TU\f\7\2\2UV\t\6\2\2VX\5\b\5\bWT\3\2\2\2")
        buf.write("X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\t\3\2\2\2[Y\3\2\2\2\\")
        buf.write("]\7\b\2\2]^\5\b\5\2^_\7\7\2\2_`\5\b\5\2`a\7\t\2\2a\13")
        buf.write("\3\2\2\2\7\17\32GRY")
        return buf.getvalue()


class STLParser ( Parser ):

    grammarFileName = "semantics.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "','", "'['", "']'", "'U_'", "'F_'", "'G_'", "'True'", 
                     "'False'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", 
                     "'!'", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "PARAMETERS", "SERIES", "LPAR", "RPAR", 
                      "COMMA", "LBRAT", "RBRAT", "U", "F", "G", "TRUE", 
                      "FALSE", "PLUS", "MINUS", "MULT", "DIV", "AND", "OR", 
                      "NOT", "EQ", "NEQ", "GT", "GE", "LT", "LE", "E", "NUMBER", 
                      "ID", "NEWLINE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_formula = 2
    RULE_expr = 3
    RULE_interval = 4

    ruleNames =  [ "prog", "stat", "formula", "expr", "interval" ]

    EOF = Token.EOF
    PARAMETERS=1
    SERIES=2
    LPAR=3
    RPAR=4
    COMMA=5
    LBRAT=6
    RBRAT=7
    U=8
    F=9
    G=10
    TRUE=11
    FALSE=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    AND=17
    OR=18
    NOT=19
    EQ=20
    NEQ=21
    GT=22
    GE=23
    LT=24
    LE=25
    E=26
    NUMBER=27
    ID=28
    NEWLINE=29
    COMMENT=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.StatContext)
            else:
                return self.getTypedRuleContext(STLParser.StatContext,i)


        def getRuleIndex(self):
            return STLParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = STLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << STLParser.PARAMETERS) | (1 << STLParser.SERIES) | (1 << STLParser.LPAR) | (1 << STLParser.F) | (1 << STLParser.G) | (1 << STLParser.TRUE) | (1 << STLParser.FALSE) | (1 << STLParser.MINUS) | (1 << STLParser.NOT) | (1 << STLParser.NUMBER) | (1 << STLParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class TextformulaContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextformula" ):
                return visitor.visitTextformula(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARAMETERS(self):
            return self.getToken(STLParser.PARAMETERS, 0)
        def EQ(self):
            return self.getToken(STLParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = STLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = STLParser.TextformulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.formula()
                self.state = 16
                self.match(STLParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = STLParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(STLParser.PARAMETERS)
                self.state = 19
                self.match(STLParser.EQ)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(STLParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = STLParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(STLParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(STLParser.NOT, 0)
        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class UContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.LPAR)
            else:
                return self.getToken(STLParser.LPAR, i)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.RPAR)
            else:
                return self.getToken(STLParser.RPAR, i)
        def U(self):
            return self.getToken(STLParser.U, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitU" ):
                return visitor.visitU(self)
            else:
                return visitor.visitChildren(self)


    class FContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def F(self):
            return self.getToken(STLParser.F, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)


    class ParensFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensFormula" ):
                return visitor.visitParensFormula(self)
            else:
                return visitor.visitChildren(self)


    class TrueFalseContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(STLParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(STLParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueFalse" ):
                return visitor.visitTrueFalse(self)
            else:
                return visitor.visitChildren(self)


    class GContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def G(self):
            return self.getToken(STLParser.G, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG" ):
                return visitor.visitG(self)
            else:
                return visitor.visitChildren(self)


    class AndOrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.LPAR)
            else:
                return self.getToken(STLParser.LPAR, i)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.RPAR)
            else:
                return self.getToken(STLParser.RPAR, i)
        def AND(self):
            return self.getToken(STLParser.AND, 0)
        def OR(self):
            return self.getToken(STLParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOr" ):
                return visitor.visitAndOr(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)

        def GT(self):
            return self.getToken(STLParser.GT, 0)
        def GE(self):
            return self.getToken(STLParser.GE, 0)
        def LT(self):
            return self.getToken(STLParser.LT, 0)
        def LE(self):
            return self.getToken(STLParser.LE, 0)
        def E(self):
            return self.getToken(STLParser.E, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = STLParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = STLParser.AndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(STLParser.LPAR)
                self.state = 27
                self.formula()
                self.state = 28
                self.match(STLParser.RPAR)
                self.state = 29
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==STLParser.AND or _la==STLParser.OR):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(STLParser.LPAR)
                self.state = 31
                self.formula()
                self.state = 32
                self.match(STLParser.RPAR)
                pass

            elif la_ == 2:
                localctx = STLParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(STLParser.NOT)
                self.state = 35
                self.match(STLParser.LPAR)
                self.state = 36
                self.formula()
                self.state = 37
                self.match(STLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = STLParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.expr(0)
                self.state = 40
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << STLParser.GT) | (1 << STLParser.GE) | (1 << STLParser.LT) | (1 << STLParser.LE) | (1 << STLParser.E))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = STLParser.ParensFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(STLParser.LPAR)
                self.state = 44
                self.formula()
                self.state = 45
                self.match(STLParser.RPAR)
                pass

            elif la_ == 5:
                localctx = STLParser.TrueFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==STLParser.TRUE or _la==STLParser.FALSE):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                localctx = STLParser.UContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(STLParser.LPAR)
                self.state = 49
                self.formula()
                self.state = 50
                self.match(STLParser.RPAR)
                self.state = 51
                self.match(STLParser.U)
                self.state = 52
                self.interval()
                self.state = 53
                self.match(STLParser.LPAR)
                self.state = 54
                self.formula()
                self.state = 55
                self.match(STLParser.RPAR)
                pass

            elif la_ == 7:
                localctx = STLParser.FContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.match(STLParser.F)
                self.state = 58
                self.interval()
                self.state = 59
                self.match(STLParser.LPAR)
                self.state = 60
                self.formula()
                self.state = 61
                self.match(STLParser.RPAR)
                pass

            elif la_ == 8:
                localctx = STLParser.GContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.match(STLParser.G)
                self.state = 64
                self.interval()
                self.state = 65
                self.match(STLParser.LPAR)
                self.state = 66
                self.formula()
                self.state = 67
                self.match(STLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(STLParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class NegNumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(STLParser.MINUS, 0)
        def NUMBER(self):
            return self.getToken(STLParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNumber" ):
                return visitor.visitNegNumber(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def PARAMETERS(self):
            return self.getToken(STLParser.PARAMETERS, 0)
        def SERIES(self):
            return self.getToken(STLParser.SERIES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class AlgOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)

        def MULT(self):
            return self.getToken(STLParser.MULT, 0)
        def DIV(self):
            return self.getToken(STLParser.DIV, 0)
        def PLUS(self):
            return self.getToken(STLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(STLParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgOp" ):
                return visitor.visitAlgOp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = STLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [STLParser.NUMBER]:
                localctx = STLParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 72
                self.match(STLParser.NUMBER)
                pass
            elif token in [STLParser.MINUS]:
                localctx = STLParser.NegNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(STLParser.MINUS)
                self.state = 74
                self.match(STLParser.NUMBER)
                pass
            elif token in [STLParser.PARAMETERS, STLParser.SERIES]:
                localctx = STLParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==STLParser.PARAMETERS or _la==STLParser.SERIES):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [STLParser.LPAR]:
                localctx = STLParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(STLParser.LPAR)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(STLParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = STLParser.AlgOpContext(self, STLParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 82
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 83
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << STLParser.PLUS) | (1 << STLParser.MINUS) | (1 << STLParser.MULT) | (1 << STLParser.DIV))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 84
                    self.expr(6) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class IntervalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRAT(self):
            return self.getToken(STLParser.LBRAT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(STLParser.COMMA, 0)

        def RBRAT(self):
            return self.getToken(STLParser.RBRAT, 0)

        def getRuleIndex(self):
            return STLParser.RULE_interval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)




    def interval(self):

        localctx = STLParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(STLParser.LBRAT)
            self.state = 91
            self.expr(0)
            self.state = 92
            self.match(STLParser.COMMA)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(STLParser.RBRAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




