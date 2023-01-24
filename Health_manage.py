def getdate():
    import datetime
    return datetime.datetime.now()

dict1={"1":"log","2":"retreve"}
dict2={"1":"Harry","2":"Rohan","3":"Parthib"}
dict3={"1":"exercise","2":"food"}

print("Health management system")
a=int(input("press 1 for log the value & press 2 for retrive" ))
if a==1:
    b=int(input("press 1 for harry 2 for rohan 3 for hammad" ))
    if b==1:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:
            d=input("type here\n" )
            f=open("Harry_exercise","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
        elif c==2:
            d=input("type here\n" )
            f=open("Harry_food","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
    elif b==2:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:
            d=input("type here\n" )
            f=open("Rohan_exercise","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
        elif c==2:
            d=input("type here\n" )
            f=open("Rohan_food","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
    elif b==3:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:
            d=input("type here\n" )
            f=open("Hammad_exercise","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
        elif c==2:
            d=input("type here\n" )
            f=open("Hammad_food","a")
            f.write(str(getdate())+" ->"+ d+"\n")
            f.close()
            print("Successfully added")
if a==2:
    b=int(input("press 1 for harry 2 for rohan 3 for hammad" ))
    if b==1:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:

            f=open("Harry_exercise")
            print(f.readlines())
            f.close()
        elif c==2:

            f=open("Harry_food")
            print(f.readlines())
            f.close()
    elif b==2:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:

            f=open("Rohan_exercise")
            print(f.readlines())
            f.close()
        elif c==2:

            f=open("Rohan_food")
            print(f.readlines())
            f.close()
    elif b==3:
        c=int(input("enter 1 for exercise 2 for food" ))
        if c==1:

            f=open("Hammad_exercise")
            print(f.readlines())
            f.close()
        elif c==2:

            f=open("Hammad_food")
            print(f.readlines())
            f.close()
