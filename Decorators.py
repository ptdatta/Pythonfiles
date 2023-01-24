# def inner1(func):
#     def inner2():
#         print("Before function execution");
#         func()
#         print("After function execution")
#     return inner2
#
# @inner1
# def function_to_be_used():
#     print("This is inside the function")
#
# function_to_be_used()


# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
# executor(print)

# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#     return nowexec
#
# @dec1
# def who_is_harry():
#     print("Harry is a good boy")
#
# # who_is_harry = dec1(who_is_harry)
# who_is_harry()


# Property decorators-->

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


# hindustani_supporter = Employee("Hindustani", "Supporter")
# # nikhil_raj_pandey = Employee("Nikhil", "Raj")
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.fname = "US"
# hindustani_supporter.lname = "hello"
#
# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)
#
# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)

skillf = Employee("Skill", "F")
print(skillf.email)
o = "this is a string"
print(id(o))    #print backend id
print(dir(skillf))      #gives all the functions of skillf


import inspect
print(inspect.getmembers(skillf))



# Some of the other common Introspects:
#
#  Functions	Working
# hasattr()	It checks if an object has an attribute.
# getattr()	It returns the contents of an attribute if there are some.
# repr()	It returns the string representation of an object
# vars()	It checks all the instance variables of an object
# issubclass()	This function checks that if a specific class is a derived class of another class.
# isinstance()	It checks if an object is an instance of a specific class.
# __doc__	This attribute gives some documentation about an object
# __name__	This attribute holds the name of the object
# callable()	This function checks if an object is a function
# help()	It checks what other functions do





