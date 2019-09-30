from pcheck.semantics.stl.STLParser import STLParser

from pcheck.semantics.stl.Semantics import Semantics


class RobSemantics(Semantics):
    EPS = 1E-15

    def atomicGT(self, lExpr, rExpr):
        return lExpr - rExpr - self.EPS

    def atomicGE(self, lExpr, rExpr):
        return lExpr - rExpr

    def atomicLT(self, lExpr, rExpr):
        return rExpr - lExpr - self.EPS

    def atomicLE(self, lExpr, rExpr):
        return rExpr - lExpr

    def atomicTrue(self):
        return float('Inf')

    def atomicFalse(self):
        return -float('Inf')

    def visitAndOr(self, ctx: STLParser.AndOrContext):
        lFormula = self.visit(ctx.formula(0))
        rFormula = self.visit(ctx.formula(1))
        if ctx.op.type == STLParser.AND:
            return min(lFormula, rFormula)
        if ctx.op.type == STLParser.OR:
            return max(lFormula, rFormula)

    def visitNot(self, ctx: STLParser.NotContext):
        return - self.visit(ctx.formula())

    def visitF(self, ctx: STLParser.FContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        return max(
            [RobSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula()) for i in
             range(i0, i1)])

    def visitG(self, ctx: STLParser.FContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        return min(
            [RobSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula()) for i in
             range(i0, i1)])

    def visitU(self, ctx: STLParser.UContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        maxVal = - float('Inf')
        values=[RobSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(0)) for i in
             range(0, i0)]
        values.append(float('Inf'))
        minF1 = min(values)
        for i in range(i0, i1 + 1):
            maxVal = max(maxVal, min(minF1,
                                     RobSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(
                                         ctx.formula(1))))
            minF1 = min(minF1,
                        RobSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(0)))
        return maxVal