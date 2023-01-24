def ispalindrone(a):
    b=str(a)
    s=0
    e=b.__len__()-1
    while(s<=e):
        if(b[s]!=b[e]):
            return False
            break
        else:
           s+=1
           e-=1
    return True


n=int(input("Enter the number of test case"))
numbers=[]
for i in range(n):
    e=int(input())
    numbers.append(e)


number=[]
for i in numbers:
    while(True):
        if(ispalindrone(i)):
              number.append(i)
              break
        else:
             i+=1

print(number)

