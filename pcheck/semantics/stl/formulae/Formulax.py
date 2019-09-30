from collections import Callable

from pcheck.semantics.stl.formulae import FormulaVisitor


class Formula():
    def accept(self, formula_visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0) -> Callable:
        pass

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        pass


class AtomicFormula(Formula):
    def __init__(self, atomic_formula: tuple) -> None:
        self.atomic_formula = atomic_formula

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_atomic(self, spatial_parameters, current_state)

    def __str__(self) -> str:
        return '(' + ' '.join(str(i) for i in self.atomic_formula) + ')'

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        spatial_paramters.add(self.atomic_formula[2])
        return interval_parameters, spatial_paramters


class AndFormula(Formula):
    def __init__(self, first_argument: Formula, second_argument: Formula) -> None:
        self.first_argument = first_argument
        self.second_argument = second_argument

    def accept(self, formula_visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return formula_visitor.visit_and_formula(self.first_argument, self.second_argument, spatial_parameters,
                                                 interval_parameters, current_state)

    def __str__(self) -> str:
        return str(self.first_argument) + " /\\ " + str(self.second_argument)

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.first_argument.collect_parameters(interval_parameters, spatial_paramters)
        self.second_argument.collect_parameters(interval_parameters, spatial_paramters)
        return interval_parameters, spatial_paramters


class OrFormula(Formula):
    def __init__(self, first_argument: Formula, second_argument: Formula) -> None:
        self.first_argument = first_argument
        self.second_argument = second_argument

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_or_formula(self.first_argument, self.second_argument, spatial_parameters,
                                        interval_parameters, current_state)

    def __str__(self) -> str:
        return str(self.first_argument) + " \\/ " + str(self.second_argument)

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.first_argument.collect_parameters(interval_parameters, spatial_paramters)
        self.second_argument.collect_parameters(interval_parameters, spatial_paramters)
        return interval_parameters, spatial_paramters


class NotFormula(Formula):
    def __init__(self, argument: Formula) -> None:
        self.argument = argument

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_not_formula(self.argument, spatial_parameters, interval_parameters, current_state)

    def __str__(self) -> str:
        return "!" + str(self.argument)

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.argument.collect_parameters(interval_parameters, spatial_paramters)
        return interval_parameters, spatial_paramters


class FinallyFormula(Formula):
    def __init__(self, argument: Formula, interval: str) -> None:
        self.interval = interval
        self.argument = argument

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_finally_formula(self.argument, self.interval, spatial_parameters, interval_parameters,
                                             current_state)

    def __str__(self) -> str:
        return "F_" + str(self.interval) + "(" + str(self.argument) + ") "

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.argument.collect_parameters(interval_parameters, spatial_paramters)
        interval_parameters.add(self.interval)
        return interval_parameters, spatial_paramters


class GloballyFormula(Formula):
    def __init__(self, argument: Formula, interval: str) -> None:
        self.interval = interval
        self.argument = argument

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_globally_formula(self.argument, self.interval, spatial_parameters, interval_parameters,
                                              current_state)

    def __str__(self) -> str:
        return "G_" + str(self.interval) + " " + str(self.argument)

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.argument.collect_parameters(interval_parameters, spatial_paramters)
        interval_parameters.add(self.interval)
        return interval_parameters, spatial_paramters


class UntilFormula(Formula):
    def __init__(self, first_argument: Formula, second_argument: Formula, interval: str) -> None:
        self.interval = interval
        self.first_argument = first_argument
        self.second_argument = second_argument

    def __str__(self) -> str:
        return str(self.first_argument) + " U_" + str(self.interval) + " " + str(self.second_argument)

    def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
               current_state: float = 0):
        return visitor.visit_until_formula(self.first_argument, self.second_argument, self.interval, spatial_parameters,
                                           interval_parameters, current_state)

    def collect_parameters(self, interval_parameters: set, spatial_paramters: set):
        self.first_argument.collect_parameters(interval_parameters, spatial_paramters)
        self.second_argument.collect_parameters(interval_parameters, spatial_paramters)
        interval_parameters.add(self.interval)
        return interval_parameters, spatial_paramters
