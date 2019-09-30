from collections import Callable


class Domain(object):

    def atomic(self, argument: Callable) -> Callable:
        pass

    def conjunction(self, left: Callable, right: Callable) -> Callable:
        pass

    def disjunction(self, left: Callable, right: Callable) -> Callable:
        pass

    def negation(self, argument: Callable) -> Callable:
        pass

    def ge(self):
        pass

    def le(self):
        pass

    def gt(self):
        pass

    def lt(self):
        pass


class DoubleDomain(Domain):

    def ge(self):
        return lambda x, y: x - y

    def le(self):
        return lambda x, y: y - x

    def gt(self):
        return lambda x, y: x - y - 1E-15

    def lt(self):
        return lambda x, y: y - x - 1E-15

    def atomic(self, argument: Callable):
        return argument

    def conjunction(self, left: tuple, right: tuple):
        # return lambda signal: lambda x: min(left(signal)(x), right(signal)(x))
        # return lambda x: min(left(x), right(x))
        return min(left[0], right[0]), min(left[1], right[1])

    def disjunction(self, left: tuple, right: tuple):
        # return lambda x: max(left(x), right(x))
        return max(left[0], right[0]), max(left[1], right[1])

    def negation(self, argument: tuple):
        return -argument[1], -argument[0]


class BooleanDomain(Domain):

    def atomic(self, argument: Callable):
        return lambda x: argument(x) > 0

    def conjunction(self, left: Callable, right: Callable):
        return lambda x: left(x) and right(x)

    def disjunction(self, left: Callable, right: Callable):
        return lambda x: left(x) or right(x)

    def negation(self, argument: Callable):
        return lambda x: not argument(x)
