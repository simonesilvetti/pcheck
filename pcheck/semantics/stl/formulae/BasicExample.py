from pcheck.semantics.stl.formulae.Domain import *
from pcheck.semantics.stl.formulae.FormulaVisitor import *
from pcheck.semantics.stl.formulae.Formulax import *
from pcheck.semantics.stl.formulae.Predicates import *
from pcheck.series.TimeSeries import *

trajectory1 = {'T': [1, 2, 3], 'X': [1, 2, 3], 'Y': [-10, -1, 3]}

trajectory = TimeSeriesFactory().fromDic(trajectory1)

spatial_parameters = lambda p, q: {'p': p, 'q': q}
interval_parameters = lambda t0, t1: {'int1': (t0, t1)}
monitor1 = TemporalMonitoring(DoubleDomain(), trajectory)
# traslate = Traslate(10)
# monitor2 = TemporalMonitoring(atomic_predicates, DoubleDomain(), timeSerie)

atomic_fromula1 = AtomicFormula(('X', Ge(), 'p'))
atomic_fromula2 = AtomicFormula(('Y', Le(), 'q'))
anDFormula = AndFormula(atomic_fromula1, atomic_fromula2)
composed = FinallyFormula(anDFormula, 'int1')
print("formula PSTL:  " + str(composed))
# print("assegno i parametri:  " + str((interval_parameters, spatial_parameters)))
# print("formula STL:  " + str(composed.accept(Printer(), spatial_parameters, interval_parameters)))
robustness = lambda t0, t1, p, q: composed.accept(monitor1, spatial_parameters(p, q), interval_parameters(t0, t1))
print("Robustness:  " + str(robustness(1, 2, 1, 2)))

# print("Robustness:  " + str(composed.accept(monitor1, spatial_parameters, interval_parameters)))
