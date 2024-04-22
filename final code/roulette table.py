import random
def simulate(each_bet,bet ):
    #american version
    choice  = [0 ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]   # 37 -- > 00
    sim = random.choice(choice)
    if(sim %2 and  sim!=37 and sim!=0 ):
        if(bet == "red"):
            return each_bet
    else:
        if(bet == "black" and  sim!=0 and sim!=37):
            return each_bet
    return -each_bet

def main():
    money = 100
    each_bet: int = 10
    bet = "red"
    avg = 0
    for i in range(10000):
        current = 100
        while True:
            current+=simulate(each_bet , bet )
            if current == 200 or current == 0:
                avg+=current
                break
    print("expected return is " , avg/10000)

if __name__ == "__main__":
    main()
#