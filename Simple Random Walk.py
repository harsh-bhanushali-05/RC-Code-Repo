import random
import matplotlib.pyplot as plt
def plotit(l):
    plt.plot(range(len(l)), l)
    print("The simulation ended with final position as : ",l[len(l)-1])
    plt.show()
def simulate():
    t = 999
    l = [0] # stores where we are present
    for i in range(t):
        r= random.choice([1,-1])
        l.append(l[i-1]+r)
    plotit(l)
def main():
    simulate()
if __name__ == "__main__":
    main()