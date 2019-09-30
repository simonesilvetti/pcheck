from pcheck.semantics.stl.STLParser import STLParser
from pcheck.semantics.stl.STLVisitor import STLVisitor


class Semantics(STLVisitor):
    def __init__(self, memory=None, timeSeries=None, currentState=0):
        if memory is None:
            memory = {}
        self.memory = memory
        self.timeSeries = timeSeries
        self.currentState = currentState

    def visitNumber(self, ctx: STLParser.NumberContext):
        return float(ctx.NUMBER().getText())

    def visitNegNumber(self, ctx: STLParser.NegNumberContext):
        return - float(ctx.NUMBER().getText())

    def visitAssign(self, ctx: STLParser.AssignContext):
        pName = ctx.PARAMETERS().getText()
        pValue = self.visit(ctx.expr())
        self.memory[pName] = pValue
        return pValue

    def visitId(self, ctx: STLParser.IdContext):
        if ctx.op.type == STLParser.PARAMETERS:
            pName = ctx.PARAMETERS().getText()
            if pName in self.memory:
                return self.memory[pName]
        elif ctx.op.type == STLParser.SERIES:
            vName = ctx.SERIES().getText()
            if vName in self.timeSeries.getVars():
                return self.timeSeries.findValueVarAtT(vName, self.currentState)

    def visitParensExpr(self, ctx: STLParser.ParensExprContext):
        return self.visit(ctx.expr())

    def visitAlgOp(self, ctx: STLParser.AlgOpContext):
        lExpr = self.visit(ctx.expr(0))
        rExpr = self.visit(ctx.expr(1))
        if ctx.op.type == STLParser.MULT:
            return lExpr * rExpr
        elif ctx.op.type == STLParser.DIV:
            return lExpr / rExpr
        elif ctx.op.type == STLParser.PLUS:
            return lExpr + rExpr
        elif ctx.op.type == STLParser.MINUS:
            return lExpr - rExpr

    def visitTextformula(self, ctx: STLParser.TextformulaContext):
        return self.visit(ctx.formula())

    def visitParensFormula(self, ctx: STLParser.ParensFormulaContext):
        return self.visit(ctx.formula())

    def visitTrueFalse(self, ctx: STLParser.TrueFalseContext):
        if ctx.op.type == STLParser.TRUE:
            return self.atomicTrue()
        elif ctx.op.type == STLParser.FALSE:
            return self.atomicTrue()

    def visitAtom(self, ctx: STLParser.AtomContext):
        lExpr = self.visit(ctx.expr(0))
        rExpr = self.visit(ctx.expr(1))
        if ctx.op.type == STLParser.GT:
            return self.atomicGT(lExpr, rExpr)
        elif ctx.op.type == STLParser.GE:
            return self.atomicGE(lExpr, rExpr)
        elif ctx.op.type == STLParser.LT:
            return self.atomicLT(lExpr, rExpr)
        elif ctx.op.type == STLParser.LE:
            return self.atomicLE(lExpr, rExpr)
        elif ctx.op.type == STLParser.E:
            return self.atomicEE(lExpr, rExpr)

    def atomicGT(self, lExpr, rExpr):
        pass

    def atomicGE(self, lExpr, rExpr):
        pass

    def atomicLT(self, lExpr, rExpr):
        pass

    def atomicLE(self, lExpr, rExpr):
        pass

    def atomicEE(self, lExpr, rExpr):
        pass

    def atomicTrue(self):
        pass

    def atomicFalse(self):
        pass