import numpy as np
import matplotlib.pyplot as plt
import random
from wavefunctions import *
from enum import Enum

if __name__ == "__main__":
    main()
    
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
    
