# 1st method
# me="Parthib"
# a="this is %s"%me
# print(a)

# 2nd method
a="this is {1} {0}"
b=a.format("Parthib",1)
print(b)

# 3rd method
# F strings
import math

me = "Harry"
a1 = 3
a = f"this is {me} {a1} {math.cos(65)}"
print(a)

