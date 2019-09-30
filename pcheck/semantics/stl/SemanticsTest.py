import unittest

import numpy as np
from antlr4 import InputStream


from pcheck.semantics.stl.BooleanSemantics import BooleanSemantics
from pcheck.semantics.stl.RobSemantics import RobSemantics
from pcheck.semantics.stl.STLLexer import STLLexer, CommonTokenStream
from pcheck.semantics.stl.STLParser import STLParser
from pcheck.semantics.stl.ZeroSemantics import ZeroSemantics
from pcheck.series.TimeSeries import TimeSeries


class TestSemantics(unittest.TestCase):

    timeSeries = TimeSeries(['P', 'Q'],
                            np.array([0, 1, 2, 3, 4]),
                            np.array([[5, 67, -6, -1, -1],
                                      [3, 3, -3, -1, -1]]))

    def setUp(self):
        pass

    def testZeroSemantics(self):
        #1
        expr = InputStream('P>4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = ZeroSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertEqual(result, 1E-10)
        #2
        expr = InputStream('P<=4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = ZeroSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertEqual(result, -1E-10)
        #3
        expr = InputStream('F_[1,3](P<=4)\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = ZeroSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertEqual(result, 0.5)

    def testRobSemantics(self):
        # 1
        expr = InputStream('P>4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = RobSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertAlmostEqual(result, 1.0,delta=1E-15)
        # 2
        expr = InputStream('P<=4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = RobSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertAlmostEqual(result, -1.0, delta=1E-15)
        # 3
        expr = InputStream('F_[1,3](P<=4)\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = RobSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertAlmostEqual(result, 10, delta=1E-15)
        # 4
        expr = InputStream('(P>0)U_[0,3](P<=Q)\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = RobSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertAlmostEqual(result, 3, delta=1E-15)

    def testBooleanSemantics(self):
        # 1
        expr = InputStream('P>4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = BooleanSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertTrue(result)
        # 2
        expr = InputStream('P<=4\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = BooleanSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertFalse(result)
        # 3
        expr = InputStream('F_[1,3](P<=4)\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = BooleanSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertTrue(result)
        # 4
        expr = InputStream('(P>0)U_[0,3](P<=Q)\n')
        lexer = STLLexer(input=expr)
        token_stream = CommonTokenStream(lexer)
        parser = STLParser(token_stream)
        tree = parser.prog()
        visitor = BooleanSemantics(timeSeries=self.timeSeries, currentState=0)
        result = visitor.visit(tree)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
