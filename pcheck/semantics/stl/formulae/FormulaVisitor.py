from functools import reduce

from pcheck.semantics.stl.formulae import Domain
from pcheck.semantics.stl.formulae.Formulax import AtomicFormula, Formula
from pcheck.series import TimeSeries


class FormulaVisitor(object):
    def visit_atomic(self, argument: Formula, parameters: dict, current_state: float = 0):
        pass

    def visit_and_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                          current_state: float = 0):
        pass

    def visit_or_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                         current_state: float = 0):
        pass

    def visit_not_formula(self, argument, spatial_parameters: dict, interval_parameter: dict, current_state: float = 0):
        pass

    def visit_finally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                              current_state: float = 0):
        pass

    def visit_globally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                               current_state: float = 0):
        pass

    def visit_until_formula(self, first_argument, second_argument, interval: str,
                            spatial_parameters: dict, interval_parameter: dict, current_state: float = 0):
        pass


class TemporalMonitoring(FormulaVisitor):
    def __init__(self, domain: Domain, time_series: TimeSeries = None,
                 current_state: float = 0, memory: dict = None) -> None:
        self.domain = domain
        self.time_series = time_series
        self.current_state = current_state
        if memory is None:
            memory = {}
        self.memory = memory

    def visit_atomic(self, formula: AtomicFormula, parameters: dict, current_state: float = 0) -> tuple:
        atom = formula.atomic_formula
        fun = atom[1].apply(self.domain)
        value = fun(self.time_series.getT(current_state)[atom[0]], parameters[atom[2]])
        return value, value
        # fun = self.domain.atomic(atomic_predicates[formula.atomic_id](parameters))
        # value = fun(self.time_series)(current_state)
        # return value, value

    def visit_and_formula(self, first_argument: Formula, second_argument: Formula, parameters: dict,
                          interval_parameter: dict, current_state: float = 0) -> tuple:
        left_value = first_argument.accept(self, parameters, interval_parameter, current_state)
        right_value = second_argument.accept(self, parameters, interval_parameter, current_state)
        return self.domain.conjunction(left_value, right_value)

        # return self.domain.conjunction(first_argument.accept(self, parameters, interval_parameter, current_state),
        #                                second_argument.accept(self, parameters, interval_parameter, current_state))

    def visit_or_formula(self, first_argument: Formula, second_argument: Formula, parameters: dict,
                         interval_parameter: dict, current_state: float = 0) -> tuple:
        left_value = first_argument.accept(self, parameters, interval_parameter, current_state)
        right_value = second_argument.accept(self, parameters, interval_parameter, current_state)
        return self.domain.disjunction(left_value, right_value)
        # return self.domain.disjunction(first_argument.accept(self, parameters, interval_parameter),
        #                                second_argument.accept(self, parameters, interval_parameter))

    def visit_not_formula(self, argument: Formula, parameters: dict, interval_parameter: dict,
                          current_state: float = 0) -> tuple:
        value = argument.accept(self, parameters, interval_parameter, current_state)
        return self.domain.negation(value)
        # return self.domain.negation(argument.accept(self, parameters, interval_parameter))

    def visit_finally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                              current_state: float = 0) -> tuple:
        (t0, t1) = interval_parameter[interval_id]
        [i0, i1] = self.time_series.findIndexesIterval(current_state + t0, current_state + t1)
        values = [argument.accept(self, spatial_parameters, interval_parameter,
                                  self.time_series.getTimes()[i] - current_state) for i in
                  range(i0, i1 + 1)]
        if current_state + t1 > self.time_series.getTimes()[-1]:
            values.append((-float('inf'), float('inf')))
        return reduce(self.domain.disjunction, values)
        # return lambda x: max(
        #     [argument.accept(self, spatial_parameters, interval_parameter,
        #                      self.time_series.getTimes()[i] - current_state)(x) for i in
        #      range(i0, i1 + 1)])

    def visit_globally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                               current_state: float = 0) -> tuple:
        (t0, t1) = interval_parameter[interval_id]
        [i0, i1] = self.time_series.findIndexesIterval(current_state + t0, current_state + t1)
        values = [argument.accept(self, spatial_parameters, interval_parameter,
                                  self.time_series.getTimes()[i] - current_state) for i in
                  range(i0, i1 + 1)]
        if current_state + t1 > self.time_series.getTimes()[-1]:
            values.append((-float('inf'), float('inf')))
        return reduce(self.domain.conjunction, values)
        # return lambda x: min(
        #     [argument.accept(self, spatial_parameters, interval_parameter,
        #                      self.time_series.getTimes()[i] - current_state)(x) for i in
        #      range(i0, i1)])

    def visit_until_formula(self, first_argument, second_argument, interval_id: str, spatial_parameters: dict,
                            interval_parameter: dict, current_state: float = 0) -> tuple:
        (t0, t1) = interval_parameter[interval_id]
        init = self.time_series.findIndexAtT(current_state)
        [i0, i1] = self.time_series.findIndexesIterval(current_state + t0, current_state + t1)
        values = [first_argument.accept(self, spatial_parameters, interval_parameter,
                                        self.time_series.getTimes()[i] - current_state) for i in
                  range(init, i0)]

        values = reduce(self.domain.conjunction, values)
        for i in range(i0, i1 + 1):
            a = list()
            a.append(values)
            appo = a
            appo.append(second_argument.accept(self, spatial_parameters, interval_parameter,
                                               self.time_series.getTimes()[i] - current_state))
            appo = reduce(self.domain.conjunction, appo)
            a = list();
            a.append(appo)
            appo = a
            appo.append(first_argument.accept(self, spatial_parameters, interval_parameter,
                                              self.time_series.getTimes()[i] - current_state))
            values = reduce(self.domain.disjunction, appo)

        a = list()
        a.append(values)
        appo = a
        if current_state + t1 > self.time_series.getTimes()[-1]:
            appo.append((-float('inf'), float('inf')))
        return reduce(self.domain.disjunction, appo)


class Printer(FormulaVisitor):

    def visit_atomic(self, argument, parameters: dict, current_state: float = 0):
        return '(' + ' '.join(
            str(parameters[i]) if i in parameters.keys() else str(i) for i in argument.atomic_formula) + ')'

    def visit_and_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                          current_state: float = 0):
        first = first_argument.accept(Printer(), spatial_parameters, interval_parameter)
        second = second_argument.accept(Printer(), spatial_parameters, interval_parameter)
        return first + " /\\ " + second

    def visit_or_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                         current_state: float = 0):
        first = first_argument.accept(Printer(), spatial_parameters, interval_parameter)
        second = second_argument.accept(Printer(), spatial_parameters, interval_parameter)
        return first + " \\/ " + second

    def visit_not_formula(self, argument, spatial_parameters: dict, interval_parameter: dict, current_state: float = 0):
        return "!" + argument.accept(Printer(), spatial_parameters, interval_parameter)

    def visit_finally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                              current_state: float = 0):
        return "F_" + str(interval_parameter[interval_id]) + "(" + argument.accept(Printer(), spatial_parameters,
                                                                                   interval_parameter) + ")"

    def visit_globally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                               current_state: float = 0):
        return "G_" + str(interval_parameter[interval_id]) + "(" + argument.accept(Printer(), spatial_parameters,
                                                                                   interval_parameter) + ")"

    def visit_until_formula(self, first_argument, second_argument, interval_id: str, spatial_parameters: dict,
                            interval_parameter: dict, current_state: float = 0):
        return first_argument.accept(Printer(), spatial_parameters, interval_parameter) + "U_" + str(
            interval_parameter[interval_id]) + second_argument.accept(Printer(), spatial_parameters,
                                                                      interval_parameter) + ")"


class Traslate(FormulaVisitor):

    def __init__(self, th: float, memory: set = None) -> None:
        self.th = th
        if memory is None:
            memory = set()
        self.memory = memory

    def visit_atomic(self, formula: AtomicFormula, parameters: dict, current_state: float = 0) -> dict:
        atom = formula.atomic_formula
        if atom[2] not in self.memory:
            self.memory.add(atom[2])
            parameters[atom[2]] = atom[1].add(self.th)(parameters[atom[2]])

    def visit_and_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                          current_state: float = 0):
        first_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)
        second_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)

    def visit_or_formula(self, first_argument, second_argument, spatial_parameters: dict, interval_parameter: dict,
                         current_state: float = 0):
        first_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)
        second_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)

    def visit_not_formula(self, argument, spatial_parameters: dict, interval_parameter: dict, current_state: float = 0):
        argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)

    def visit_finally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                              current_state: float = 0):
        argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)

    def visit_globally_formula(self, argument, interval_id: str, spatial_parameters: dict, interval_parameter: dict,
                               current_state: float = 0):
        argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)

    def visit_until_formula(self, first_argument, second_argument, interval_id: str, spatial_parameters: dict,
                            interval_parameter: dict, current_state: float = 0):
        first_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)
        second_argument.accept(Traslate(self.th, self.memory), spatial_parameters, interval_parameter)
