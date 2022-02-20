import numpy as np
import matplotlib.pyplot as plt
import random
from wavefunctions import *
from enum import Enum

if __name__ == "__main__":
    main()

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
    def __init__(self, xMin, xMax, yMin, yMax, zMin, zMax, n, func1, func2):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.zMin = zMin
        self.zMax = zMax
        self.n = n
        self.func1 = func1
        self.func2 = func2
        self.integral = 0.0
        self.coordTupleList = []
        self.valList = []

    def monteCarloIntegrate(self):
        offset = 5.0
        # print(self.n)
        for i in range(self.n):
            xCur = random.uniform(self.xMin, self.xMax)
            yCur = random.uniform(self.yMin, self.yMax)
            zCur = random.uniform(self.zMin, self.zMax)

            self.coordTupleList.append((xCur,yCur)) # Print xy projection

            # ensure defined behavior for phi
            if xCur == 0.0 and yCur == 0.0:
                xCur = 0.0000001
                yCur = 0.0000001

            LHV = self.func1(xCur + (offset / 2), yCur, zCur)
            RHV = self.func2(xCur - (offset / 2), yCur, zCur)
            prod = LHV * RHV
            self.valList.append(prod)

        vol = BoundingBox.volumeFromLimits(
            self.xMin,self.xMax,self.yMin,self.yMax,self.zMin,self.zMax)
        avg = self.calculateAvg()
        # Use average value theorem
        self.integral = vol * avg

    def calculateAvg(self):
        return sum(self.valList)/len(self.valList)

def visualize(funVals, coords):
    rLayer1 = []
    rLayer2 = []
    rLayer3 = []
    rLayer4 = []
    bLayer1 = []
    bLayer2 = []
    bLayer3 = []
    bLayer4 = []
    for i, val in enumerate(funVals):
        if val > 0:
            # red
            if val < 1e-4:
                rLayer4.append(coords[i])
            elif val < 1e-3:
                rLayer3.append(coords[i])
            elif val < 1e-2:
                rLayer2.append(coords[i])
            else:
                rLayer1.append(coords[i])
        else:
            # blue
            if val < -1e-4:
                bLayer4.append(coords[i])
            elif val < -1e-3:
                bLayer3.append(coords[i])
            elif val < -1e-2:
                bLayer2.append(coords[i])
            else:
                bLayer1.append(coords[i])

    rX1 = [t[0] for t in rLayer1]
    rY1 = [t[1] for t in rLayer1]
    rX2 = [t[0] for t in rLayer2]
    rY2 = [t[1] for t in rLayer2]
    rX3 = [t[0] for t in rLayer3]
    rY3 = [t[1] for t in rLayer3]
    rX4 = [t[0] for t in rLayer4]
    rY4 = [t[1] for t in rLayer4]
    
    bX1 = [t[0] for t in bLayer1]
    bY1 = [t[1] for t in bLayer1]
    bX2 = [t[0] for t in bLayer2]
    bY2 = [t[1] for t in bLayer2]
    bX3 = [t[0] for t in bLayer3]
    bY3 = [t[1] for t in bLayer3]
    bX4 = [t[0] for t in bLayer4]
    bY4 = [t[1] for t in bLayer4]
    
    plt.scatter(rX1,rY1, np.full(len(rY1), 2), alpha=1.00, color="Red")
    plt.scatter(rX2,rY2, np.full(len(rY2), 2), alpha=0.75, color="Red")
    plt.scatter(rX3,rY3, np.full(len(rY3), 2), alpha=0.50, color="Red")
    plt.scatter(rX4,rY4, np.full(len(rY4), 2), alpha=0.25, color="Red")

    plt.scatter(bX1,bY1, np.full(len(bY1), 2), alpha=1.00, color="Blue")
    plt.scatter(bX2,bY2, np.full(len(bY2), 2), alpha=0.75, color="Blue")
    plt.scatter(bX3,bY3, np.full(len(bY3), 2), alpha=0.50, color="Blue")
    plt.scatter(bX4,bY4, np.full(len(bY4), 2), alpha=0.25, color="Blue")
    
            

def main():
    minBound = -10
    maxBound = 10
    integrals = []
    nTot = 100000
    monte = MonteCarlo(
        minBound,maxBound,minBound,maxBound,minBound,maxBound,
        nTot,psi1s,psi2px)
    monte.monteCarloIntegrate()
    integrals.append(monte.integral)
        
    # print("Integral: {}".format(sum(integrals)/len(integrals)))
    visualize(monte.valList, monte.coordTupleList)
    # for item in monte.coordTupleList:
        # print(item)
    plt.show()
    
