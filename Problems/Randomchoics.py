import random

a=int(input())
b=int(input())
c=random.randint(a,b)
print("Player 1:")
i=1;
print(f"Enter  a number btw {a} and {b}")
while(True):
    e=int(input())
    if(e==c):
        print(f"You correct it by {i} trials")
        break
    elif(e>c):
        print("Get a smaller number")
    else:
        print("Get a bigger number")
    i+=1

d=random.randint(a,b)
print("Player 2:")
j=1;
print(f"Enter  a number btw {a} and {b}")
while(True):
    e=int(input())
    if(e==d):
        print(f"You correct it by {j} trials")
        break
    elif(e>d):
        print("Get a smaller number")
    else:
        print("Get a bigger number")
    j+=1

if(i>j):
    print("Player 2 won")
elif(i==j):
    print("Draw")
else:
    print("Player 1 won")