from pcheck.semantics.stl.formulae import Domain


class Predicates:
    def apply(self, domain: Domain):
        pass

    def add(self, value: float) -> callable:
        pass


class Ge(Predicates):

    def apply(self, domain: Domain):
        return domain.ge()

    def __str__(self) -> str:
        return ">="

    def add(self, value: float) -> callable:
        return lambda x: x + value


class Le(Predicates):
    def apply(self, domain: Domain):
        return domain.le()

    def __str__(self) -> str:
        return "<="

    def add(self, value: float) -> callable:
        return lambda x: x - value


class Gt(Predicates):
    def apply(self, domain: Domain):
        return domain.gt()

    def __str__(self) -> str:
        return ">"

    def add(self, value: float) -> callable:
        return lambda x: x + value


class Lt(Predicates):
    def apply(self, domain: Domain):
        return domain.lt()

    def __str__(self) -> str:
        return "<"

    def add(self, value: float) -> callable:
        return lambda x: x - value


class AtomicPredicates():
    def __init__(self, variable: str, predicate: Predicates, th: float) -> None:
        self.th = th
        self.predicate = predicate
        self.variable = variable

    def translate(self, delta: float) -> tuple:
        f = self.predicate.add(delta)
        return self.variable, self.predicate, f(self.th)