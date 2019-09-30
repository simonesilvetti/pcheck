# Generated from STL.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .STLParser import STLParser
else:
    from STLParser import STLParser

# This class defines a complete generic visitor for a parse tree produced by STLParser.

class STLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by STLParser#prog.
    def visitProg(self, ctx:STLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#textformula.
    def visitTextformula(self, ctx:STLParser.TextformulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#assign.
    def visitAssign(self, ctx:STLParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#blank.
    def visitBlank(self, ctx:STLParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#AndOr.
    def visitAndOr(self, ctx:STLParser.AndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#Not.
    def visitNot(self, ctx:STLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#Atom.
    def visitAtom(self, ctx:STLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#parensFormula.
    def visitParensFormula(self, ctx:STLParser.ParensFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#trueFalse.
    def visitTrueFalse(self, ctx:STLParser.TrueFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#U.
    def visitU(self, ctx:STLParser.UContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#F.
    def visitF(self, ctx:STLParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#G.
    def visitG(self, ctx:STLParser.GContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#number.
    def visitNumber(self, ctx:STLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#NegNumber.
    def visitNegNumber(self, ctx:STLParser.NegNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#id.
    def visitId(self, ctx:STLParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#parensExpr.
    def visitParensExpr(self, ctx:STLParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#AlgOp.
    def visitAlgOp(self, ctx:STLParser.AlgOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#interval.
    def visitInterval(self, ctx:STLParser.IntervalContext):
        return self.visitChildren(ctx)



del STLParser