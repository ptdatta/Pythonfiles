n=int(input("Enter a number "))
b=input("Enter true or false ")

def pattern(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print("* ",end="")
        print("\n")
    return

def rpattern(n):
    for i in range(1,n+1,1):
        for j in range(n+1,i,-1):
            print("* ",end="")
        print("\n")
    return

if(b=="true"):
    pattern(n)
elif(b=="false"):
    rpattern(n)
else:
    print("Invalid input")

