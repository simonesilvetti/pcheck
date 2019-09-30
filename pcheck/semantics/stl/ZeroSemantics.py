from pcheck.semantics.stl.STLParser import STLParser

from pcheck.semantics.stl.Semantics import Semantics


class ZeroSemantics(Semantics):
    EPS = 1E-10

    def atomicGT(self, lExpr, rExpr):
        if lExpr > rExpr:
            return self.EPS
        else:
            return - self.EPS

    def atomicGE(self, lExpr, rExpr):
        if lExpr >= rExpr:
            return self.EPS
        else:
            return - self.EPS

    def atomicLT(self, lExpr, rExpr):
        if lExpr < rExpr:
            return self.EPS
        else:
            return - self.EPS

    def atomicLE(self, lExpr, rExpr):
        if lExpr <= rExpr:
            return self.EPS
        else:
            return - self.EPS

    def atomicEE(self, lExpr, rExpr):
        if lExpr == rExpr:
            return self.EPS
        else:
            return - self.EPS

    def atomicTrue(self):
        return self.EPS

    def atomicFalse(self):
        return -self.EPS
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
        if i0 == i1:
            if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(ctx.formula()) > 0:
                return 1
            else:
                return - self.EPS
        support = 0
        if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(ctx.formula()) > 0:
            support += self.timeSeries.getTimes()[i0 + 1] - (self.currentState + t0)
        for i in range(i0 + 1, i1):
            val = ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula())
            if val > 0:
                support += (self.timeSeries.getTimes()[i + 1] - self.timeSeries.getTimes()[i])
        if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i1]).visit(ctx.formula()) > 0:
            support += (self.currentState + t1) - self.timeSeries.getTimes()[i1]
        if support > 0:
            return support / (t1 - t0)
        else:
            return - self.EPS

    def visitG(self, ctx: STLParser.GContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        return self.localG(t0, t1, ctx.formula())

    def localG(self, t0, t1, formula):
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        if i0 == i1:
            if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(formula) > 0:
                return self.EPS
            else:
                return - 1
        support = 0
        if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(formula) < 0:
            support += - (self.timeSeries.getTimes()[i0 + 1] - (self.currentState + t0))
        for i in range(i0 + 1, i1):
            val = ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(formula)
            if val < 0:
                support += - (self.timeSeries.getTimes()[i + 1] - self.timeSeries.getTimes()[i])
        if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i1]).visit(formula) < 0:
            support += -((self.currentState + t1) - self.timeSeries.getTimes()[i1])
        if support < 0:
            return support / (t1 - t0)
        else:
            return self.EPS

    def visitU(self, ctx: STLParser.UContext):
        t0 = self.visit(ctx.interval().expr(0))
        t1 = self.visit(ctx.interval().expr(1))
        if self.localG(0, t0, ctx.formula(0)) < 0:
            return -self.EPS
        support = 0
        [i0, i1] = self.timeSeries.findIndexesIterval(self.currentState + t0, self.currentState + t1)
        if i0 == i1 and ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(
                ctx.formula(1)) > 0:
            return 1
        if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i0]).visit(ctx.formula(1)) > 0:
            support += self.timeSeries.getTimes()[i0 + 1] - t0
        i = i0 + 1
        while i < i1 and ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(
                ctx.formula(0)) > 0:
            if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(1)) > 0:
                support += (self.timeSeries.getTimes()[i + 1] - self.timeSeries.getTimes()[i])
            i += 1
        if i == i1 and ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(
                ctx.formula(0)) > 0:
            if ZeroSemantics(self.memory, self.timeSeries, self.timeSeries.getTimes()[i]).visit(ctx.formula(1)) > 0:
                support += (t1 - self.timeSeries.getTimes()[i])
        if support > 0:
            return support / (t1 - t0)
        else:
            return -self.EPS

