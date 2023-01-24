# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print("The sum of these two numbers is",
#           int(num1)+int(num2))
# # except Exception as e:
# #     print(e)
# except Exception:
#     print("Invalid input")



f1 = open("harry.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f.close()
    f1.close()

print("Important stuff")



