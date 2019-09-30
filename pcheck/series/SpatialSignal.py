class SpatialSignal:
    def __init__(self, lmap):
        self.lmap = lmap

    def get(self, l):
        return self.lmap[l]

    def map(self, f):
        return SpatialSignal({l: f(v) for (l,v) in self.lmap.items()})

    def merge(self, f, other):
        return SpatialSignal({l: f(v, other.lmap[l]) for (l, v) in self.lmap.items()})