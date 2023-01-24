i=0
# while(i<45):
#     print(i)
#     i+=2


while(True):
    i=i+1
    if(i==5):
        continue
    if(i>10):
        break
    print(f"The value of i is : {i}")

# enter a num greater than 100
while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
