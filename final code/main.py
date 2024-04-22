import math
import  matplotlib.pyplot  as plt
import pandas as pd
from scipy.stats import kurtosis

data = "BSE Indices Historical.csv"
df = pd.read_csv(data)
def print_data():
    print(df)

def get_mean():
    open = df['Open']
    mean  = 0
    for i in open:
        mean+=i
    mean/=open.size
    return mean


def get_moving_mean(tau):
    open = df['Open']
    l=[]
    for i in range(open.size - tau):
        mean_curr = 0
        for j in range(tau):
            mean_curr+=open[i+j]
        mean_curr/=tau
        l.append(mean_curr)
    return l

def get_variance():
    var = 0
    mean = get_mean()
    open = df['Open']
    for i in open:
        var+=(i-mean) **2
    var=var/open.size
    return var

def get_moving_variance(tau):
    open = df['Open']
    l = get_moving_mean(tau)
    var_list = []
    for i in range(open.size - tau):
        var = 0
        for j in range(tau):
            var+=(open[i+j] - l[i])**2
        var/=tau
        var_list.append(var)
    return var_list

def get_standard_deviation():
    var = get_variance()
    return math.sqrt(var)

def get_moving_standard_deviation(tau):
    var = get_moving_variance(tau)
    l = []
    for i in var:
        l.append(math.sqrt(i))
    return l


def get_skewness():
    mean = get_mean()
    std= get_standard_deviation()
    open  = df['Open']
    n=open.size
    mul=n/((n-1)*(n-2))
    sig=0
    for i in open:
       sig+=((i-mean)/std)**3
    return sig*mul



def get_moving_skewness(tau):
    open_prices = df['Open']
    skewness_list = []
    for i in range(len(open_prices) - tau + 1):
        window = open_prices[i : i + tau]
        mean = sum(window) / tau
        m3 = sum((x - mean) ** 3 for x in window) / tau
        m2 = sum((x - mean) ** 2 for x in window) / tau
        if m2 != 0:
            skewness = m3 / (m2 ** 1.5)
        else:
            skewness = 0
        skewness_list.append(skewness)
    return skewness_list


def get_kurtosis():
    mean = get_mean()
    std = get_standard_deviation()
    open_prices = df['Open']
    n = open_prices.size
    constant1 = n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))
    constant2 = 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    kurtosis = constant1 * sum(((x - mean) / std) ** 4 for x in open_prices) - constant2
    return kurtosis

def get_moving_kurtosis(tau):
    moving_mean= get_moving_mean(tau)
    moving_std = get_moving_standard_deviation(tau)
    open = df['Open']
    n=tau
    constant1 = n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))
    constant2 = 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    kurtosis= []
    for i in range(open.size-tau):
        sum = 0
        for j in range( tau ):
            sum+= (((open[i+j]-moving_mean[i]) / moving_std[i])**4 )
        sum *=constant1
        sum -= constant2
        kurtosis.append(sum)
    return  kurtosis


def get_entropy():
    mean = get_mean()
    std = get_standard_deviation()
    entropy = 0.5 * math.log(2 * math.pi * math.e * std**2)
    return entropy

def get_moving_entropy(tau):
    std = get_moving_standard_deviation(tau)
    ans = []
    for i in std:
       entropy = 0.5 * math.log(2 * math.pi * math.e * i ** 2)
       ans.append(entropy)
    return ans


def get_kutosis_with_library():
    data = df['Open']
    kurtosis_value = kurtosis(data, fisher=True)
    print("Population Kurtosis:", kurtosis_value)

def plot_moving_skewness(tau):
    skewness_list = get_moving_skewness( tau)
    date = df['Date'][:len(skewness_list)]
    plt.bar(date, skewness_list)
    plt.xlabel('Date')
    plt.ylabel(f'Moving Skewness (Tau={tau})')
    plt.title(f'Moving Skewness with Tau={tau}')
    plt.xticks(rotation=45)  # Optional: Rotate the x-axis labels for better readability
    plt.show()


def plot_data():
    l = df['Open']
    date = df['Date'][:len(l)]
    plt.bar(date, l)
    plt.xlabel('Date')
    plt.ylabel(f'Moving Mean)')
    plt.title(f'Moving Mean with ')
    plt.show()


def plot_moving_mean(tau):
    l=get_moving_mean(tau)
    date = df['Date'][:len(l)]
    plt.bar(date,l)
    plt.xlabel('Date')
    plt.ylabel(f'Moving Mean (Tau={tau})')
    plt.title(f'Moving Mean with Tau={tau}')
    plt.show()


def plot_moving_variance(tau):
    l=get_moving_variance(tau)
    date = df['Date'][:len(l)]
    plt.bar(date,l)
    plt.xlabel('Date')
    plt.ylabel(f'Moving variance (Tau={tau})')
    plt.title(f'Moving variance with Tau={tau}')
    plt.show()


def plot_moving_standard_deviation(tau):
    l=get_moving_standard_deviation(tau)
    date = df['Date'][:len(l)]
    plt.bar(date,l)
    plt.xlabel('Date')
    plt.ylabel(f'Moving standard deviation  (Tau={tau})')
    plt.title(f'Moving standard deviation with Tau={tau}')
    plt.show()

def plot_moving_kurtosis(tau):
    list= get_moving_kurtosis(tau)
    date = df['Date'][:len(list)]
    plt.plot(date, list)
    plt.xlabel('Date')
    plt.ylabel(f'Moving kurtosis (Tau={tau})')
    plt.title(f'Moving kurtosis with Tau={tau}')
    plt.show()
def plot_moving_kurtosis_usingLibary(tau):
    data = df['Open']
    moving_kurtosis = data.rolling(window=5).kurt()
    print(moving_kurtosis)
    return moving_kurtosis


if __name__ == '__main__':
    # print(print_data())
    # print(get_moving_mean())
    # print(get_variance())
    # print(get_mean())
    # print(get_moving_standard_diviation(5))
    # plot_moving_mean(5)
    # plot_moving_variance(5)
    # print(get_skewness())
    # plot_moving_standard_diviation(5)
    # print(get_kurtosis())
    # get_kutosis_with_library()
    # print(get_moving_kurtosis(5))
    # print(plot_moving_kurtosis(5))
    # print(plot_moving_kurtosis(5))
    # plot_moving_kurtosis_usingLibary(5)
    print(plot_moving_kurtosis(500))