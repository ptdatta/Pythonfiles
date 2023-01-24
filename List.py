list = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]
print(list[4])
print(list[1:6:2])

# List Methods :
l1=[1,-9,78,5,63,2,-4,17,45]       #l1 is a list
l1.sort()
print(l1)      #l1 after sorting
l1.reverse()
print(l1)      #l1 after reversing all elements


# List Methods :-
list1=[1,2,3,6,5,4]     #list1 is a list

list1.append(7)    # This will add 7 in the last of list
list1.insert(3,8)    # This will add 8 at 3 index in list
list1.remove(1)    #This will remove 1 from the list
list1.pop(2)     #This will delete and return index 2 value.
print(list1)
print(list1.pop(2))


# Tuples in Python :
a=()    # It's an example of empty tuple
x=(1,)   # Tuple with single value i.e. 1
tup1 = (1,2,3,4,5)
tup1 = ('harry', 5, 'demo', 5.8)
#tup1[2]=9      tuple value does not change
print(tup1)


# Swapping of two numbers :
a = 10
b = 15
print(a,b)     #It will give output as: 10 15
a,b = b,a
print(a,b)     #It will give output as: 15 10



# sort(): Sorts the list in ascending order.
# type(list): It returns the class type of an object.
# append(): Adds a single element to a list.
# extend(): Adds multiple elements to a list.
# index(): Returns the first appearance of the specified value.
# max(list): It returns an item from the list with max value.
# min(list): It returns an item from the list with min value.
# len(list): It gives the total length of the list.
# list(seq): Converts a tuple into a list.
# cmp(list1, list2): It compares elements of both lists list1 and list2.