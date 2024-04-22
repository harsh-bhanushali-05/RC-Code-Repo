# comparing the variation with and without monte carlo
import math
import numpy as np
def InCircle(points , radius ):
    [x,y]=points
    return x**2 + y**2 <= radius**2
def Monte(dat , radius ):
    list = []
    for i in range(0, 1000000 , 10000 ):
        list.append(nonMonte(dat[i:i+10000] , radius))
    return sum(list)/len(list)
def nonMonte(dat,radius ):
    count = 0
    for points in dat:
        if InCircle(points,radius):
            count+=1
    A = count / len(dat)
    totalArea = radius * 2 * radius * 2
    return A*totalArea
def main():
    radius = 100
    dat = np.random.rand(1000000,2) *(radius*2)-radius
    NonArea = nonMonte(dat , radius )
    MonthArea = Monte(dat,radius )
    real= math.pi * radius * radius
    print(NonArea)
    print(MonthArea)
    print(" Monte error " ,math.fabs(MonthArea - real))
    print(" Non Monte error " ,math.fabs(NonArea - real))
    print(" if value is +ve then monte did better " ,math.fabs(NonArea - real) - math.fabs(MonthArea - real)  )
if __name__ == "__main__":
    main()
