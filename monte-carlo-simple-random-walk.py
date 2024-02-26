import random
def simulate():
    choice = [1 ,-1]
    pos = 0
    for i in range(1000):
        pos=pos+random.choice(choice)
    return pos
def monte_carlo(data):
    window_size = 30
    num_windows = len(data) // window_size
    averages = []
    for i in range(num_windows):
        window = data[i * window_size : (i + 1) * window_size]
        window_average = sum(window) / window_size
        averages.append(window_average)
    return sum(averages) / len(averages)

def main():
    list =[]
    for i in range(10000):
        list.append(simulate())
    avg = sum(list)/len(list)
    print( f"The avg is {avg}")
    print(f" The ans acc to monte carlo {monte_carlo(list)}")

if __name__ == "__main__":
    main()