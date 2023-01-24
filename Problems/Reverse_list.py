a=list(input())
s=0;
e=a.__len__()-1
while(s<=e):
    temp=a[s]
    a[s]=a[e]
    a[e]=temp
    s+=1
    e-=1

print(a)