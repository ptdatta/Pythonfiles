n=int(input())
mn=int(input())
mx=int(input())
for i in range(mn,mx+1,1):
    if(n%i==0):
        print(f"{i} is a divisor of {n}")
    else:
        print(f"{i} is not a divisor of {n}")