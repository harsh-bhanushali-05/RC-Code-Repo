import random
import matplotlib.pyplot as plt
import numpy as np
def roll():
    return random.randint(1,6)
def getAllRoll():
    val=[]
    for i in range(100000):
        val.append(roll())
    return val
def getMean(list):
    s=sum(list)
    return s/len(list)
def batchMean():
    allMean = []
    list= getAllRoll()
    for i in range(0,100000,10):
        allMean.append(getMean(list[i:i+10]))
        i=i+1000
    return allMean
def main ():
    dist= batchMean()
    f, bins, _ = plt.hist(dist, bins=100, weights=np.ones_like(dist) / len(dist))
    plt.xlabel('X')
    plt.ylabel('Relative Frequency')
    plt.show()
if __name__ == "__main__":
    main()