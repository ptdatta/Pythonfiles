#Small dictionary
# hello=input()
# d2={"abandoned":"ruined","mutable":"can change","unmutable":"con't change","recognized":"to know anyone"}
# print("meaning is",end="->")
# print ( d2[hello])


# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      420:"Kababs",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d2["Rohan"])
print(d2[420])
print(d2)
del d2[420]
print(d2["Shubham"])
d3 = d2.copy()
del d3["Harry"]
print(d3)
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())
