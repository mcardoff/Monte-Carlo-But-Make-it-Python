import numpy as np
import random as random
from enum import Enum

class Spin(Enum):
    Up = 1
    Down = 0

class BoundingBox():
    @staticmethod
    def calculateVolume(l1,l2,l3):
        return l1*l2*l3

    @staticmethod
    def volumeFromLimits(xMin,xMax,yMin,yMax,zMin,zMax):
        l1 = max(xMin, xMax) - min(xMin,xMax)
        l2 = max(yMin, yMax) - min(yMin,yMax)
        l3 = max(zMin, zMax) - min(zMin,zMax)
        return BoundingBox.calculateVolume(l1,l2,l3)

class MonteCarlo():
    def __init__(self, xMin, xMax, yMin, yMax, zMin, zMax, n, spacing, func):
        assert(isinstance(n,int))
        self.xMin = xMin; self.xMax = xMax;
        self.yMin = yMin; self.yMax = yMax
        self.zMin = zMin; self.zMax = zMax
        self.n = n; self.spacing = spacing; self.func = func; self.integral = 0.0
        self.coordTupleList = []; self.valList = []

    def monteCarloIntegrate(self):
        # n points
        for i in range(self.n):
            # generate a random point
            xCur = random.uniform(self.xMin, self.xMax)
            yCur = random.uniform(self.yMin, self.yMax)
            zCur = random.uniform(self.zMin, self.zMax)

            self.coordTupleList.append((xCur,yCur)) # Print xy projection

            # ensure defined behavior for phi
            if xCur == 0.0 and yCur == 0.0:
                xCur = 0.0000001
                yCur = 0.0000001

            # eval function at this point
            fval = self.func(xCur,yCur,zCur,self.spacing)
            # save it so we can calc an average
            self.valList.append(fval)

        # volume of our defined space
        vol = BoundingBox.volumeFromLimits(
            self.xMin,self.xMax,self.yMin,self.yMax,self.zMin,self.zMax
        )
        avg = self.calculateAvg()
        # Use average value theorem: Integral = Volume * Avg Value
        self.integral = vol * avg

    def calculateAvg(self):
        return sum(self.valList)/len(self.valList)
