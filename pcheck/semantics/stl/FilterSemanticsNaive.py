from pycheck.semantics.STL.STLParser import STLParser
from pycheck.semantics.STL.STLVisitor import STLVisitor
import numpy as np
__author__ = 'ssilvetti'


class FilterSemanticsNaive(STLVisitor):
    def __init__(self, memory=None, series=None, currentState=0):
        if memory is None:
            memory = {}
        self.memory = memory
        self.series=series
        self.currentState = currentState

    def visitAssign(self, ctx):
        name = ctx.PARAMETERS().getText()
        value = float(self.visit(ctx.expr()))
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.formula())
        print(value)
        return 0

    def visitParensFromula(self, ctx:STLParser.ParensFromulaContext):
        return self.visit(ctx.formula())

    def visitParensExpr(self, ctx: STLParser.ParensExprContext):
        return self.visit(ctx.expr())

    def visitNumber(self, ctx: STLParser.NumberContext):
        return float(ctx.NUMBER().getText())

    def visitNegNumber(self, ctx: STLParser.NegNumberContext):
        return - float(ctx.NUMBER().getText())

    def visitId(self, ctx):
        if ctx.op.type == STLParser.PARAMETERS:
            name = ctx.PARAMETERS().getText()
            if name in self.memory:
                return self.memory[name]
        else:
            name = ctx.SERIES().getText()
            if name in self.series.getVars():
                index = self.series.getVars().index(name)
                return self.series.getMatrix()[self.currentState,index]
        return 0


    def visitMulDiv(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if ctx.op.type == STLParser.MULT:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if ctx.op.type == STLParser.PLUS:
            return left + right
        return left - right

    def visitAndOr(self, ctx: STLParser.AndOrContext):
        left = bool(self.visit(ctx.formula(0)))
        right = bool(self.visit(ctx.formula(1)))
        if ctx.op.type == STLParser.OR:
            return float(np.max([left,right]))
        return float(np.min([left,right]))


        # Visit a parse tree produced by grammarProvaParser#Not.

    def visitNot(self, ctx: STLParser.NotContext):
        return -(self.visit(ctx.formula()))


        # Visit a parse tree produced by grammarProvaParser#Atom.

    def visitAtom(self, ctx: STLParser.AtomContext):
        left = float(self.visit(ctx.expr(0)))
        right = float(self.visit(ctx.expr(1)))
        if ctx.op.type == STLParser.GE:
            return left-right
        elif ctx.op.type == STLParser.GT:
            return left - right-1E-15
        elif ctx.op.type == STLParser.LT:
            return right - left-1E-15
        else:
            return right - left  #TODO unificare

    def visitMitl(self, ctx: STLParser.MitlContext):
        return self.visit(ctx.mitlTerm())

    def visitU(self, ctx: STLParser.UContext):
        t0=float(self.visit(ctx.timeBound().expr(0)))
        t1=float(self.visit(ctx.timeBound().expr(1)))
        s = self.series
        indext0 = s.indexFloor(self.currentState,t0) #forse è meglio cambiarla sta funzione.
        indext1 = s.indexFloor(self.currentState,t1,indext0)
        #indext1 = min(indext1+1,len(s))
        min0 = float('inf')

        for i in range(self.currentState,min(indext0, len(s))):
            visitor = FilterSemanticsNaive(self.memory, s, i)
            value = visitor.visit(ctx.formula(0))
            if (value < min0):
                min0 = value
        sum = 0
        for i in range(min(indext0, len(s)), min(indext1 + 1, len(s))):
            visitor = FilterSemanticsNaive(self.memory, s, i)
            value = visitor.visit(ctx.formula(0))
            if (value < min0):
                min0 = value
            maxInner=np.min([min0,visitor.visit(ctx.formula(1))])
            sum +=  maxInner * (s.times[i + 1] - s.times[i])
        return float(sum)
        # return [sumPositive / (indext1 - indext0), sumNegative / (indext1 - indext0)]


        # Visit a parse tree produced by grammarProvaParser#F.

    def visitF(self, ctx: STLParser.FContext):
        t0 = float(self.visit(ctx.timeBound().expr(0)))
        t1 = float(self.visit(ctx.timeBound().expr(1)))
        s = self.series
        indext0 = s.indexFloor(self.currentState, t0)  # forse è meglio cambiarla sta funzione.
        indext1 = s.indexFloor(self.currentState, t1, indext0)
        # indext1 = min(indext1 + 1, len(s))
        sum=0
        for i in range(self.currentState, indext1):
            value = FilterSemanticsNaive(self.memory, s, i).visit(ctx.formula())
            sum += value * (s.times[i + 1] - s.times[i])
        return float(sum/(indext1-indext0))



    def visitG(self, ctx: STLParser.GContext):
        t0 = float(self.visit(ctx.timeBound().expr(0)))
        t1 = float(self.visit(ctx.timeBound().expr(1)))
        s = self.series
        indext0 = s.indexFloor(self.currentState, t0)  # forse è meglio cambiarla sta funzione.
        indext1 = s.indexFloor(self.currentState, t1, indext0)
        #indext1 = min(indext1 + 1, len(s))
        min = float('inf')
        for i in range(self.currentState, indext1):
            value = FilterSemanticsNaive(self.memory, s, i);
            if(value<min):
                min=value
        return float(min)