class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")
print(emp2/emp1)
print(emp2)      #Prefers str 1st
print(repr(emp1))


# Operation	Syntax	Function
# Addition	a + b	add(a, b)
# Concatenation	seq1 + seq2	concat(seq1, seq2)
# Containment Test	o in seq	contains(seq, o)
# Division	a / b	div(a, b) # without __future__.division
# Division	a / b	truediv(a, b) # with __future__.division
# Division	a // b	floordiv(a, b)
# Bitwise And	a & b	and_(a, b)
# Bitwise Exclusive Or	a ^ b	xor(a, b)
# Bitwise Inversion	~ a	invert(a)
# Bitwise Or	a | b	or_(a, b)
# Exponentiation	a ** b	pow(a, b)
# Identity	a is b	is_(a, b)
# Identity	a is not b	is_not(a, b)
# Indexed Assignment	o[k] = v	setitem(o, k, v)
# Indexed Deletion	del o[k]	delitem(o, k)
# Indexing	o[k]	getitem(o, k)
# Left Shift	a << b	lshift(a, b)
# Modulo	a % b	mod(a, b)
# Multiplication	a * b	mul(a, b)
# Negation (Arithmetic)	- a	neg(a)
# Negation (Logical)	not a	not_(a)
# Right Shift	a >> b	rshift(a, b)
# Sequence Repitition	seq * i	repeat(seq, i)
# Slice Assignment	seq[i:j] = values	setslice(seq, i, j, values)
# Slice Deletion	del seq[i:j]	delslice(seq, i, j)
# Slicing	seq[i:j]	getslice(seq, i, j)
# String Formatting	s % o	mod(s, o)
# Subtraction	a - b	sub(a, b)
# Truth Test	o	truth(o)
# Ordering	a < b	lt(a, b)
# Ordering	a <= b	le(a, b)
# Equality	a == b	eq(a, b)
# Difference	a != b	ne(a, b)
# Ordering	a >= b	ge(a, b)
# Ordering	a > b	gt(a, b)


# Web link-->  http://davis.lbl.gov/Manuals/PYTHON-2.4.3/lib/operator-map.html  (Chart)
#              https://docs.python.org/2/library/operator.html
