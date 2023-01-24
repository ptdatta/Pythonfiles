def read_number(self):
    print(self.num)

# read_number()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)



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


harry = Employee("Harry", 255, "Instructor")
parthib=Employee("Parthib",566,"Softwere Engineer")
kunal=Employee.from_dash("Kunal-568-Devops Engineer")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# parthib.no_of_leaves=89
parthib.changes_leaves(56)
print(harry.salary)
print(parthib.role)
print(parthib.no_of_leaves)
print(harry.no_of_leaves)
print(harry.printdetails())
print(parthib.printdetails())
print(kunal.printdetails())
harry.printgood("hello")



"""
Abstraction-> refers to hiding unnecessary details to focus on the whole product instead of parts of the project
 separately. It is a mechanism that represents the important features without including implementation details. 
 Abstraction helps us in partitioning the program into many independent concepts so we may hide the irrelevant 
 information in the code. It offers the greatest flexibility when using abstract data-type objects in different 
 situations.
 
Encapsulation-> means hiding under layers. When working with classes and handling sensitive data, global access
 to all the variables used in the program is not secure. In Encapsulation, the internal representation of an 
 object is generally hidden from the outside to secure the data. It improves the maintainability of an application
 and helps the developers to organize the code better.
 


Abstraction-> is used to solve the problem and issues that arise at the design stage.

Encapsulation-> is used to solve the problem and issue that arise at the implementation stage.

Abstraction-> focuses on what the object does instead of how the details are implemented.

Encapsulation-> focuses on hiding the code and data into a single unit to secure the data from the outside world.

 Abstraction-> can be implemented by using Interface and Abstract Class.

Encapsulation-> can be implemented using Access Modifiers (Public, Protected, and Private.)

Abstraction-> Its application is during the design level.

Encapsulation-> Its application is during the Implementation level.


"""
