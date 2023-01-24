def digits(n):
    s=str(n)
    p=s.__len__()
    return p


a=int(input("what is your age"))
s=digits(a)
if(s<3):
    print(f"You will be 100 in {100-a} years")
elif(s==3):
    if(a==100):
        print("you are already 100")
    else:
        print("You maybe the oldest person alive")
elif(s==4 and s<2021):
    print(f"you will be 100 in {a+100}")
else:
    print("you are not even born")