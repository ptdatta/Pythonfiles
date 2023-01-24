#Public-->
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Protected-->
class employee:
    def __init__(self, name, age):
        self._name = name            #Single'_'
        self._age = age

# Private-->
class employee:
    def __init__(self, name, age):
        self.__name = name           #Double '__'
        self.__age = age


# Example:
class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

Harry=Employee()
Harry._protec=45
print(Harry._protec)
Harry.__pr=8    #this create a new variable
print(Harry._Employee__pr)   #access private variable
print(Harry.__pr)
