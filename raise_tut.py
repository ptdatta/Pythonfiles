# a=input("what's your name?")
# b=input("how much do you earn")
#
# if int(b)==0:
#     raise  ZeroDivisionError("b= 0 so program stopped")
# if a.isnumeric():
#     raise Exception("num not allowed")
#
# print(f"hello {a}")

c=input("enter your name")
try:
    print(a)

except Exception as e:
    if c=="harry":
        raise  ValueError("harry is blocked he is not allowed")

    print("exception handled")