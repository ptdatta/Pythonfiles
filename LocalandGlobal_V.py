# def sum():
#     a = 10  # local variable cannot be accessed outside the function
#     b = 20
#     sum = a + b
#     print(sum)
# # print(a)  # this gives an error
# sum()


# a=1  #global variable
# def print_Number():
#             a=4
#             a=a+1;
#             print(a)
# print_Number()
# print(a)


# l = 10 # Global
# def function1(n):
#     l = 5 #Local
#     m = 8 #Local
#     # global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
# function1("This is me")
# print(m)


x = 89
def harry():
    x = 20
    def rohan():
        # global x
        x = 88
        print("value of x in rohan",x)
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)






