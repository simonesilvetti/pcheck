import numpy as np


class TimeSeries:
    def __init__(self, var, times, matrix):
        self.vars = var
        self.times = times
        self.matrix = matrix

    def __len__(self):
        return len(self.times)

    def getVars(self):
        return self.vars

    def getMatrix(self):
        return self.matrix

    def getTimes(self):
        return self.times

    def findIndexAtT(self, t):
        for index in range(0, len(self.times)):
            if (self.times[index] > t):
                return index - 1
        return len(self.times) - 1

    def findIndexesIterval(self, t0, t1):
        if t0 >= self.times[len(self.times) - 1]:
            return [len(self.times) - 1, len(self.times) - 1]
        for index in range(0, len(self.times)):
            if (self.times[index] > t0):
                i0 = index - 1
                break
        if t1 >= self.times[len(self.times) - 1]:
            return [i0, len(self.times) - 1]
        for index in range(i0, len(self.times)):
            if (self.times[index] > t1):
                i1 = index - 1
                return [i0, i1]

    def findValueVarAtT(self, var, t):
        iTime = self.findIndexAtT(t)
        iVar = self.vars.index(var)
        return self.matrix[iVar][iTime]

    def getT(self, t):
        iTime = self.findIndexAtT(t)
        # return {self.vars[i]: self.matrix[i][iTime] for i in range(len(self.vars))}
        return dict(zip(self.vars, self.matrix[:, iTime]))


class TimeSeriesFactory:

    def fromDic(self, trajectory: dict) -> TimeSeries:
        times = trajectory['T']
        del trajectory['T']
        return TimeSeries(list(trajectory.keys()), times, np.array(list((trajectory.values()))))
