
import json
a ={"name":"harry","salary":9000,"language":"Python"}
# conversion to JSON done by dumps() function
b = json.dumps(a)
print(b) # printing the output



data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(parsed)

#Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=2, sort_keys=True))
# indent = spaces
# sort_keys=sorted or not
