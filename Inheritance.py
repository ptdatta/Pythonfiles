class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def changes_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
         return cls(*string.split("-"))    #In one line

    @staticmethod
    def printgood(string):
        print("This is good " + string)

# Single Inheritance
class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}." \
               f"The languages are {self.languages}"

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

# Multiple Inheritance
class CoolProgramer(Player,Employee):   #which class is 1st written printdetailes will run for that

    language = "C++"
    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])

kunal = Player("Kunal", ["Cricket"])
parthib = CoolProgramer("Parthib", ["Football","Video games"])

print(karan.printprog())
print(karan.printdetails())
# print(harry.printprog())     will not run
parthib.printlanguage()
print(kunal.var)
print(kunal.printdetails())
print(parthib.printdetails())
print("Multilevel Inhertance\n\n-->")


# Multilevel Inheritance
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
carry = Grandson()
print(carry.basketball)
print(carry.isdance())

# print(darry.guitar)

# electronic device
# pocket gadget
# phone





# Single Inheritance-->
# class Parent():
#     def first(self):
#         print('Parent function')
#
# class Child(Parent):
#     def second(self):
#         print('Child function')
#
# object1 = Child()
# object1.first()
# object1.second()


# Multiple Inheritance-->
# class Base1:
#     def func1(self):
#         print("this is Base1 class")
#
#
# class Base2:
#     def func2(self):
#         print("this is Base2 class")
#
#
# class Child(Base1, Base2):
#     def func3(self):
#         print("this is Base3 class")
#
#
# obj = Child()
# obj.func1()
# obj.func2()
# obj.func3()


# Multilevel Inherance-->
# class level1:
#     def first(self):
#         print('code')
#
#
# class level2(level1):  # inherit level1
#     def second(self):
#         print('with')
#
#
# class level3(level2):  # inherit level2
#     def third(self):
#         print('harry')
#
#
# obj = level3()
# obj.first()
# obj.second()
# obj.third()


"""
Multiple inheritance-->

1.Multiple Inheritance is where a class inherits from more than one base class.
2.Sometimes, multiple Inheritance makes the system more complex, that’s why it is not widely used.
3.Multiple Inheritance has two class levels; these are base class and derived class.


Multilevel inheritance-->

1.In multilevel inheritance, we inherit from a derived class, making that derived class a base class for a new class.
2.Multilevel Inheritance is widely used. It is easier to handle code when using multilevel inheritance.
3.Multilevel Inheritance has three class levels, which are base class, intermediate class, and derived class.
"""


# Diamond shape inheritance-->
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")

a = A()
b = B()
c = C()
d = D()

d.met()



