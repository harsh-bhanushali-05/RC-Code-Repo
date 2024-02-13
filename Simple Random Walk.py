import random
import matplotlib.pyplot as plt
def plotit(l):
    plt.plot(range(len(l)), l)
    print("The simulation ended with final position as : ",l[len(l)-1])
    plt.show()
def simulate(profit , loss ):
    t = 100000000000000
    l = [0] # stores where we are present
    for i in range(t):
        r= random.choice([1,-1])
        l.append(l[i-1]+r)
        #add these lines to terminate process after winning or lossing 100
        if(l[len(l)-1] == profit or l[len(l)-1]==loss):
          return l[len(l)-1]
def get_prob(profit , loss ):
    ans =[]
    for i in range(1000):
        ans.append(simulate(profit,loss))
    count  = 0
    for i in ans:
        if(i == profit):
            count+=1
    print(count/len(ans))
def main():
    # simulate()
    get_prob(100,-50)
if __name__ == "__main__":
    main()