from pcheck.semantics.stl.STLParser import STLParser
from pcheck.semantics.stl.Semantics import Semantics


class BooleanSemantics(Semantics):

    def atomicGT(self, lExpr, rExpr):
        return lExpr>rExpr

    def atomicGE(self, lExpr, rExpr):
        return lExpr>=rExpr

    def atomicLT(self, lExpr, rExpr):
        return lExpr<rExpr

    def atomicLE(self, lExpr, rExpr):
        return lExpr<=rExpr

    def atomicTrue(self):
        return True

    def atomicFalse(self):
        return False

    def visitAndOr(self, ctx: STLParser.AndOrContext):
        lFormula = self.visit(ctx.formula(0))
        rFormula = self.visit(ctx.formula(1))
        if ctx.op.type == STLParser.AND:
            return lFormula and rFormula
        if ctx.op.type == STLParser.OR:
            return lFormula or rFormula

    def visitNot(self, ctx: STLParser.NotContext):
        return not self.visit(ctx.formula())

    def visitF(self, ctx: STLParser.FContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        for i in range(i0,i1):
            if(BooleanSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula())):
                return True
        return False

    def visitG(self, ctx: STLParser.FContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        for i in range(i0,i1):
            if(not BooleanSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula())):
                return False
        return True

    def visitU(self, ctx: STLParser.UContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        for i in range(0,i0):
            if(not BooleanSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(0))):
                return False
        i=i0
        while i<=i1:
            if BooleanSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(1)):
                return True
            if(not BooleanSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(0))):
                return False
            i+=1
        return False