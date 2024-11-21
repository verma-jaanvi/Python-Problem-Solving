fruits=["mango","apple","kiwi","orange","banana"]

def finding(word,fruits):
    new=[]
    print("\nguess the letter in the word: ")
    letter= input()
    word = word + letter
    print("the guess is ", word ,":")
    for x in fruits:
        if word in x:
            new.append(x)
            
    if(len(new)>1):
        print("\nchoices are:")
        for x in new:
            for y in x:
                if y in word:
                    print(y,end="")
                else:
                    print("-",end="")
            print("  ", end=" ")
        finding(word,fruits)
    elif(len(new)==1):
        print("right answer: ", new[0])
    else:
        print("word not found")

def adding():
    print("do you want to add new fruit element: [y/n]")
    ans=input()
    if ans=='y':
        print("enter the fruit name:")
        return fruits.append(input())
    else:
        return fruits


word=""
print("here you have to guess the name of the fruit in the list also you can add more name to it.")
adding()
finding(word,fruits)
