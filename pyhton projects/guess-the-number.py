#guess the number
import random
def guess(num,i):

    if (i<=10):
        print("\nEnter your guess:")
        gus=int(input())
        # print(i)
        if(num==gus):
            if(i==0):
                print("bingo, jackpot")
                return 0
            elif(i==1):
                print("awesome, thats right")
                return 0
            elif(i==2):
                print("hurray, great guess")
                return 0
            elif(i==3):
                print("excellent, you did it")
                return 0
            elif(i==4):
                print("nice, that's right")
                return 0
            elif(i==5):
                print("well done,right answer")
                return 0
            else:
                print("right answer! you won!")
                return 0
        elif(gus>num):
            if (gus-num)>=30:
                print("oops! too high")
            elif (gus-num)>10:
                print("umhm, high")
            else:
                print("close, but high")
            guess(num,i+1)
        else:
            if (num-gus)>=30:
                print("oops! too low")
            elif (num-gus)>10:
                print("umhm, low")
            else:
                print("close, but low")
            guess(num,i+1)
    else:
        print("runs exhausted\nyou lose!!\nnice try, next time!")
    return 0
    

print("guess the number between 1 to 100: ")
num = int(random.random()*100)
# print(num)
print("you have 10 tries to get the number\nGood luck :) ")

guess(num,1)