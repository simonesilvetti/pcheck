# from typing import Callable
#
# from pcheck.series.TimeSeries import TimeSeriesFactory
#
#
# class Interval(object):
#
#     def __init__(self, interval_id: str) -> None:
#         self.interval_id = interval_id
#
#
# class FormulaVisitor(object):
#     def visit_atomic(self, argument, parameters: dict, state: int):
#         pass
#
#     def visit_and_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
#                           state: int):
#         pass
#
#     def visit_or_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
#                          state: int):
#         pass
#
#     def visit_not_formula(self, argument, spatial_parameters: dict, interval_parameter: dict, state: int):
#         pass
#
#     def visit_finally_formula(self, argument, interval: str, spatial_parameters: dict, interval_parameter: dict,
#                               state: int):
#         pass
#
#     def visit_globally_formula(self, argument, interval: str, spatial_parameters: dict, interval_parameter: dict,
#                                state: int):
#         pass
#
#     def visit_until_formula(self, argument, first_argument, second_argument, interval: str,
#                             spatial_parameters: dict, interval_parameter: dict, state: int):
#         pass
#
#
# class Formula():
#     def accept(self, formula_visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict,
#                state: int) -> Callable:
#         pass
#
#
# class AtomicFormula(Formula):
#     def __init__(self, atomic_id: str) -> None:
#         self.atomic_id = atomic_id
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int):
#         return visitor.visit_atomic(self, spatial_parameters, state)
#
#
# class AndFormula(Formula):
#     def __init__(self, first_argument: Formula, second_argument: Formula) -> None:
#         self.first_argument = first_argument
#         self.second_argument = second_argument
#
#     def accept(self, formula_visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int):
#         return formula_visitor.visit_and_formula(self.first_argument, self.second_argument, spatial_parameters,
#                                                  interval_parameters, state)
#
#
# class OrFormula(Formula):
#     def __init__(self, first_argument: Formula, second_argument: Formula) -> None:
#         self.first_argument = first_argument
#         self.second_argument = second_argument
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int):
#         return visitor.visit_or_formula(self.first_argument, self.second_argument, spatial_parameters,
#                                         interval_parameters, state)
#
#
# class NotFormula(Formula):
#     def __init__(self, argument: Formula) -> None:
#         self.argument = argument
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int):
#         return visitor.visit_not_formula(self.argument, spatial_parameters, interval_parameters, state)
#
#
# class FinallyFormula(Formula):
#     def __init__(self, argument: Formula, interval: str) -> None:
#         self.interval = interval
#         self.argument = argument
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int = 0):
#         return visitor.visit_finally_formula(self.argument, self.interval, spatial_parameters, interval_parameters,
#                                              state)
#
#
# class GloballyFormula(Formula):
#     def __init__(self, argument: Formula, interval: str) -> None:
#         self.interval = interval
#         self.argument = argument
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int = 0):
#         return visitor.visit_globally_formula(self.argument, self.interval, spatial_parameters, interval_parameters,
#                                               state)
#
#
# class UntilFormula(Formula):
#     def __init__(self, first_argument: Formula, second_argument: Formula, interval: str) -> None:
#         self.interval = interval
#         self.first_argument = first_argument
#         self.second_argument = second_argument
#
#     def accept(self, visitor: FormulaVisitor, spatial_parameters: dict, interval_parameters: dict, state: int):
#         return visitor.visit_until_formula(self.first_argument, self.second_argument, spatial_parameters,
#                                            interval_parameters, state)
#
#
# class Domain(object):
#
#     def Atomic(self, argument: Callable):
#         pass
#
#     def And(self, left: Callable, right: Callable) -> Callable:
#         pass
#
#     def Or(self, left: Callable, right: Callable) -> Callable:
#         pass
#
#     def Not(self, argument: Callable) -> Callable:
#         pass
#
#
# class DoubleDomain(Domain):
#
#     def Atomic(self, argument: Callable):
#         return argument
#
#     def And(self, left: Callable, right: Callable):
#         return lambda signal: lambda x: min(left(signal)(x), right(signal)(x))
#
#     def Or(self, left: Callable, right: Callable):
#         return lambda signal: lambda x: max(left(signal, x), right(signal, x))
#
#     def Not(self, argument: Callable):
#         return lambda signal: lambda x: -argument(signal)(x)
#
#
# class BooleanDomain(Domain):
#
#     def Atomic(self, argument: Callable):
#         return lambda x: argument(x) > 0
#
#     def And(self, left: Callable, right: Callable):
#         return lambda x: left(x) and right(x)
#
#     def Or(self, left: Callable, right: Callable):
#         return lambda x: left(x) or right(x)
#
#     def Not(self, argument: Callable):
#         return lambda x: not argument(x)
#
#
# class TemporalMonitoring(FormulaVisitor):
#     # memory=None, timeSeries=None, currentState=0
#
#     def __init__(self, atomic_predicates: dict, domain: Domain) -> None:
#         self.domain = domain
#         self.atomic_predicates = atomic_predicates
#
#     def visit_atomic(self, formula: AtomicFormula, parameters: dict, state: int):
#         return self.domain.Atomic(atomic_predicates[formula.atomic_id](parameters))
#
#     def visit_and_formula(self, first_argument: Formula, second_argument: Formula, parameters: dict,
#                           interval_parameter: dict, state: int):
#         return self.domain.And(first_argument.accept(self, parameters, interval_parameter, state),
#                                second_argument.accept(self, parameters, interval_parameter, state))
#
#     def visit_or_formula(self, first_argument: Formula, second_argument: Formula, parameters: dict,
#                          interval_parameter: dict, state: int):
#         return self.domain.Or(first_argument.accept(self, parameters, interval_parameter),
#                               second_argument.accept(self, parameters, interval_parameter))
#
#     def visit_not_formula(self, argument: Formula, parameters: dict, interval_parameter: dict, state: int):
#         return self.domain.Not(argument.accept(self, parameters, interval_parameter, state))
#
#     def visit_finally_formula(self, argument, interval: str, parameters: dict, interval_parameter: dict, state: int):
#         if (state == 0):
#             value = lambda x, signal: x
#         else:
#             value = lambda x, signal: x + signal.times[state]
#         return lambda signal: self.aggregator(max, interval_parameter[interval], state, signal,
#                                               lambda x, i: argument.accept(self, parameters, interval_parameter, i)(
#                                                   signal)(value(x, signal)))
#         # return lambda signal: lambda x: argument.accept(self, parameters, interval_parameter)(signal)(fun(x))
#
#     def visit_globally_formula(self, argument, interval: str, parameters: dict, interval_parameter: dict, state: int):
#         if (state == 0):
#             value = lambda x, signal: x
#         else:
#             value = lambda x, signal: x + signal.times[state]
#         return lambda signal: self.aggregator(min, interval_parameter[interval], state, signal,
#                                               lambda x, i: argument.accept(self, parameters, interval_parameter, i)(
#                                                   signal)(value(x, signal)))
#
#     def visit_until_formula(self, argument, first_argument, second_argument, interval: str, parameters: dict,
#                             interval_parameter: dict, state: int):
#         super().visit_until_formula(argument, first_argument, second_argument, parameters, interval_parameter)
#
#     def aggregator(self, operator, interval, state, signal, fun):
#         t0 = interval[0]
#         t1 = interval[1]
#         rang = signal.findIndexesIterval(state + t0, state + t1)
#         return lambda x: operator([fun(x, i) for i in rang])
#
#
# trajectory = {'T': [0, 1, 2], 'X': [89, 65, 75], 'Y': [0, 3, 3]}
# ts = TimeSeriesFactory().fromDic(trajectory)
# ts.getT(2.5)
# signal = lambda t: {'X': t, 'Y': 3 * t + 2}
# spatial_parameters = {'p': 0, 'q': 0}
# interval_parameters = {'int': (0, 2.5)}
# atomic_predicates = {'a': lambda d: lambda ts: lambda t: (ts.getT(t)['X'] - d['p']),
#                      'b': lambda d: lambda ts: lambda t: (ts.getT(t)['Y'] - d['q'])}
#
# doubleMonitoring = TemporalMonitoring(atomic_predicates, DoubleDomain())
# booleanMonitoring = TemporalMonitoring(atomic_predicates, BooleanDomain())
#
# atomic_fromula1 = AtomicFormula('a')
# atomic_fromula2 = AtomicFormula('b')
# andFormula = AndFormula(atomic_fromula1, atomic_fromula2)
# notFromula = NotFormula(andFormula)
# eventually = GloballyFormula(atomic_fromula1, 'int')
#
# # # f_boolean = lambda x, y: notFromula.accept(booleanMonitoring, parameters(x, y))(signal)(0)
# f_double = eventually.accept(doubleMonitoring, spatial_parameters, interval_parameters)
# print(f_double(ts)(0.1))
# # # print(f_boolean(239, 254))
