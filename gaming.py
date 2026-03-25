import random
name1=input("enter the player 1: ")
name2=input("enter the player 2: ")

d1=random.randint(1,25)
d2=random.randint(1,25)

s1=25
s2=25

print("_________PLAYER 1_______")
while(True):
    g=int(input("enter the number: "))
    s1=s1-1
    if(d1==g):
        print("YOUR GUESS IS CORRECT !!!'")
        break
    elif(d1<g):
        print("guess less!!!")
    else:
        print("guess more!!!")

print("_________PLAYER 2_______")
while True:
    g=int(input("enter the number: "))
    s2=s2-1
    if(d2==g):
        break
    elif(d2<g):
        print("guess less!!!")
    else:
        print("guess more!!!")
if(s1==s2):
    print("THE MATCH IS DRAW !!!")
elif(s1>s2):
    print ("THE WINNER IS ",name1)
else:
     print ("THE WINNER IS ",name2)