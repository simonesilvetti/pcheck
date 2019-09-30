class TimeSignal:
    def __init__(self, times, values):
        self.times = times
        self.values = values

    def get_init_time(self):
        return self.times[0]

    def get_final_time(self):
        return self.times[-1]

    def index_of(self, t):
        if t > self.times[-1]:
            return -1
        count = -1
        for t1 in self.times:
            if t1 > t:
                return count
            else:
                count += 1
        return count

    def value_at(self, t):
        i = self.index_of(t)
        if i < 0:
            return None
        else:
            return self.values[i]

    def append(self, t, v):
        self.times.append(t)
        self.values.append(v)

    def map(self, f):
        return TimeSignal(self.times, map(f, self.values))

    def merge(self, f, other):
        i_self = 0
        i_other = 0
        if self.times[i_self] < other.times[i_other]:
            i_self = self.index_of(other.times[i_other])
            t = other.times[i_other]
        else:
            i_other = other.index_of(self.times[i_self])
            t = self.times[i_self]
        while i_self < len(self.times)-1 and i_other < len(other.times)-1:
            if self.times[i_self] < other.times[i_other]:
                i_self += 1
            elif self.times[i_self] == other.times[i_other]:
                i_self += 1
                i_other += 1
            else:
                i_other += 1
        if i_self == len(self.times)-1:

        else:

        return None  # return the signal obtained by computing f(self,s2)
