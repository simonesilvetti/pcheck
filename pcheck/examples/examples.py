import numpy as np

from pcheck.semantics import stlBooleanSemantics, stlRobustSemantics
from pcheck.series.TimeSeries import TimeSeries

timeSeries = TimeSeries(['P', 'Q'],
                        np.array([0, 1, 2, 3, 4]),
                        np.array([[5, 67, -6, -1, -1],
                                  [3, 3, -3, -1, -1]]))

print(stlBooleanSemantics(timeSeries, 0, 'F_[1,3](P<=4)'))
print(stlRobustSemantics(timeSeries, 0, 'F_[1,3](P<=4)'))
print(stlRobustSemantics(timeSeries, 0, '(G_[1,2] (Q>2)) & (F_[1,3](P<=4))'))
print(stlRobustSemantics(timeSeries, 0, '(G_[1,2] (Q>2)) & (!(F_[1,3](P<=4)))'))
print(stlRobustSemantics(timeSeries, 0, '(G_[1,2] (Q>2)) | (!(F_[1,3](P<=4)))'))
print(stlRobustSemantics(timeSeries, 0, '(P<3) & (Q>2)'))