#lcm program 
def LCM(a,b):
    for i in range(max(a,b),(a*b)+1):
        if (i%a==0 and i%b==0):
            print(i)
            break
    
                

print("Enter two number to find the LCM of :")
a=int(input())
b=int(input())
print("the lcm of ",a," and ",b," is :")
LCM(a,b)