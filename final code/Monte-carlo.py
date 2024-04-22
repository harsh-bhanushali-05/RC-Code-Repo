import math
import  random
def generate(radius):
    x=random.uniform(radius*-1,radius)
    y=random.uniform(radius*-1,radius)
    return [x,y]
def getPoints(radius):
    l=[]
    for i in range(1000000):
        l.append(generate(radius))
    return l
def getDistance(x,y):
    return math.sqrt(x**2 + y**2)
def Incircle(x,y,radius):
    if getDistance(x,y)<=radius:
        return True
    return False
def TotalIncirle(radius):
    l = getPoints(radius)
    count = 0
    for [x,y]in l:
        if Incircle(x,y,radius):
            count+=1
    return count
def main():
    radius = 3;
    areaPortion = TotalIncirle(radius) / 1000000
    totalArea = radius*2 *  radius*2
    estimate = totalArea * areaPortion
    print("The radius of the circle is = ")
    print(radius)
    print("Area estimated using monte carlo= ")
    print(estimate)
    print("Area calculated using formula= ")
    print((math.pi*radius*radius))

if __name__ == "__main__":
    main()