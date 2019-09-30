from pycheck.series.SpatialSignal import SpatialSignal
from pycheck.series.TimeSignal import TimeSignal

class SpaceTimeSignal:
    def __init__(self, timeSignal):
        self.timeSignal= timeSignal

    def timeSeries_at(self, l):
        return self.timeSignal(l)

    def spatialsignal_at(self, t):
        return SpatialSignal({l: s.value_at(t) for (l,s) in self.timeSignal.items()})

