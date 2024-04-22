import numpy as np
import math
def getPoints(radius):
    random_matrix = np.random.rand(1000000, 2) * (radius*2) - radius
    return random_matrix
def getArea(radius):
    l=getPoints(radius)
    count=0
    for [x,y] in l:
        if x**2+ y**2 <= radius**2:
            count+=1
    return count
def getArea_monte(points, radius):
    count = 0
    for [x, y] in points:
        if x**2 + y**2 <= radius**2:
            count += 1
    return count

def monte(radius):
    random_matrix = np.random.rand(1000000, 2) * (radius * 2) - radius
    l = []
    for i in range(0, 1000000, 10000):
        l.append((getArea_monte(random_matrix[i:i+10000], radius)) * radius**2 * 4 / 10000)
    return sum(l) / len(l)

def answer(radius):
    count = getArea(radius)
    totalArea = radius*2 * radius*2
    areaOfCircle = count/1000000
    print(f'estimate = {areaOfCircle*totalArea}')
    monteArea=monte(radius)
    print(f'estimate using monte carlo {monteArea}')
    print(" real =",(math.pi * radius * radius))
    print(f"The error in normal estimate  ={math.fabs(areaOfCircle*totalArea - math.pi * radius * radius) }")
    print(f"The error in monte carlo {math.fabs( monteArea - math.pi * radius * radius ) }")
def main():
    radius = 100
    answer(radius)
if __name__ == "__main__":
    main()