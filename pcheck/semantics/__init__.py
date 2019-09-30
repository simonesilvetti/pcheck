from antlr4 import InputStream

from pcheck.semantics.stl.BooleanSemantics import BooleanSemantics
from pcheck.semantics.stl.RobSemantics import RobSemantics
from pcheck.semantics.stl.STLLexer import STLLexer, CommonTokenStream
from pcheck.semantics.stl.STLParser import STLParser
from pcheck.series import TimeSeries


def stlBooleanSemantics(timeSeries: TimeSeries , time: float, formula: str):
    expr = InputStream(formula + '\n')
    lexer = STLLexer(input=expr)
    token_stream = CommonTokenStream(lexer)
    parser = STLParser(token_stream)
    tree = parser.prog()
    visitor = BooleanSemantics(timeSeries=timeSeries, currentState=time)
    return visitor.visit(tree)


def stlRobustSemantics(timeSeries: TimeSeries , time: float, formula: str):
    expr = InputStream(formula + '\n')
    lexer = STLLexer(input=expr)
    token_stream = CommonTokenStream(lexer)
    parser = STLParser(token_stream)
    tree = parser.prog()
    visitor = RobSemantics(timeSeries=timeSeries, currentState=time)
    return visitor.visit(tree)
