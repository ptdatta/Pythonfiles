#join() with lists
# numList = ['1', '2', '3', '4']
# separator = ','
# print(separator.join(numList))

# myDictionary = {"name": "Jack", "country": "America"}
# separator = "_separator_"
# print(separator.join(myDictionary))

# inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
# sep = '_'
# out = sep.join(inputlist)     #all datatype of list must be same
# print(out)

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

for item in lis:
    print(item, "and", end=" ")

print("\n")
a = ", ".join(lis)
print(a, "other wwe superstars")
