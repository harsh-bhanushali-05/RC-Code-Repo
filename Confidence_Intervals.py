# code to generate confidence interval of a gaussian distribution
# replace dist to get distribution of your data
import numpy as np
import matplotlib.pyplot as plt

def getplot():
    dist = np.random.normal(0, 10, 1000000)
    f, bins, _ = plt.hist(dist, bins=100, weights=np.ones_like(dist) / len(dist))
    plt.xlabel('X')
    plt.ylabel('Relative Frequency')
    print("2 sd frequency = ", np.sum(f[(bins[:-1] >= -100) & (bins[:-1] <= 100)]))

def main():
    getplot()
    plt.show()

if __name__ == "__main__":
    main()
