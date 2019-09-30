import stochpy

from pcheck.semantics.stl.formulae.Domain import *
from pcheck.semantics.stl.formulae.FormulaVisitor import *
from pcheck.semantics.stl.formulae.Formulax import *
from pcheck.semantics.stl.formulae.Predicates import *
from pcheck.series.TimeSeries import *

smod = stochpy.SSA()
smod.Model('epidemicBackup.psc')
smod.DoStochSim(end=130, mode='time', trajectories=2)
smod.GetTrajectoryData(1)

timeSerie = TimeSeries(smod.data_stochsim.species_labels, smod.data_stochsim.time, smod.data_stochsim.species.T)
trajectory1 = {'T': [1, 2, 3], 'X': [1, 2, 3], 'Y': [-10, -1, 3]}
trajectory2 = {'T': [1, 2, 3], 'X': [7, 8, 9], 'Y': [3, 5, 2]}

ts1 = TimeSeriesFactory().fromDic(trajectory1)
ts2 = TimeSeriesFactory().fromDic(trajectory2)

spatial_parameters = {'p': 350, 'q': 30, 't': 9}
interval_parameters = {'int1': (50, 90), 'int2': (10, 50)}
# atomic_predicates = {'a': ('S', Ge, 'p'),
#                      'b': ('I', Ge, 'q')}

# atomic_predicates = {'a': lambda d: lambda ts: lambda t: (d['p'][0] * (ts.getT(t)['X'] - d['p'][1])),
#                      'b': lambda d: lambda ts: lambda t: (d['q'][0] * (ts.getT(t)['Y'] - d['q'][1]))}

monitor1 = TemporalMonitoring(DoubleDomain(), timeSerie)
# traslate = Traslate(10)
# monitor2 = TemporalMonitoring(atomic_predicates, DoubleDomain(), timeSerie)

atomic_fromula1 = AtomicFormula(('S', Ge(), 'p'))
atomic_fromula2 = AtomicFormula(('I', Ge(), 'q'))
anDFormula = AndFormula(atomic_fromula1, atomic_fromula2)
eventually = FinallyFormula(anDFormula, 'int1')
mid = OrFormula(AtomicFormula(('X', Ge(), 't')), eventually)
composed = UntilFormula(atomic_fromula1, atomic_fromula2, 'int2')
print("formula PSTL:  " + str(composed))
print("estraggo i parametri da PSTL:  " + str(composed.collect_parameters(set(), set())))
print("assegno i parametri:  " + str((interval_parameters, spatial_parameters)))
print("formula STL:  " + str(composed.accept(Printer(), spatial_parameters, interval_parameters)))
print("Robustness:  " + str(composed.accept(monitor1, spatial_parameters, interval_parameters)))
f = lambda t: composed.accept(monitor1, spatial_parameters, interval_parameters, t)
print(spatial_parameters)
robustness_before = composed.accept(monitor1, spatial_parameters, interval_parameters)
composed.accept(Traslate(robustness_before[0]), spatial_parameters, interval_parameters)
robustness_after =composed.accept(monitor1, spatial_parameters, interval_parameters)
print("Robustness after: "+str(robustness_after))
print(spatial_parameters)

# for t in np.arange(0, 160, 5):
#     print(str(t) + "::" + str(f(t)))
# )# atomic_fromula2 = AtomicFormula('b')
# anDFormula = AndFormula(atomic_fromula1, atomic_fromula2)
# eventually = GloballyFormula(anDFormula, 'int')
# f_double1 = eventually.accept(monitor1, spatial_parameters, interval_parameters, 0)
# print(f_double1)
# # f_boolean = lambda x, y: notFromula.accept(booleanMonitoring, parameters(x, y))(signal)(0)
# f_double1 = eventually.accept(monitor1, spatial_parameters(0), interval_parameters, 0)
# f_double2 = eventually.accept(monitor2, spatial_parameters(0), interval_parameters, 0)
# print(f_double1)
# print(f_double2)
# value = (f_double1[0] + f_double2[0]) / 2
#
# f_double1 = eventually.accept(monitor1, spatial_parameters(value), interval_parameters, 0)
# f_double2 = eventually.accept(monitor2, spatial_parameters(value), interval_parameters, 0)
# print(f_double1)
# print(f_double2)

# # print(f_boolean(239, 254))

# predicate = AtomicPredicates('S', Ge(), 5)
# print(str(('S', Ge(), 5)))
# print(str(predicate.translate(10)))
