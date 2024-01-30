import numpy as np
import math
def getPoints(radius):
    random_matrix = np.random.rand(10000000, 2) * (radius*2) - radius
    return random_matrix
def getArea(radius):
    l=getPoints(radius)
    count=0
    for [x,y] in l:
        if x**2+ y**2 <= radius**2:
            count+=1
    return count
def answer(radius):
    count = getArea(radius)
    totalArea = radius*2 * radius*2
    areaOfCircle = count/10000000
    print(f'estimate = {areaOfCircle*totalArea}')
    print((math.pi * radius * radius))
def main():
    radius = 5
    answer(radius)
if __name__ == "__main__":
    main()