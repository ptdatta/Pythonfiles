# list=["jkjd","jwhd","kddj","jdjd"]
# for i in range(1,4,2):
#     print(list[i])
#
# items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
#
# for i in items:
#     if str(i).isnumeric() and i>=6:
#         print(i)
#
# dict1= {"Best Python Course": "CodeWithHarry",
#         "Best C Languge Course": "CodeWithHarry",
#         "Harry Sir":"Tom Cruise Of Programming"
#         }
#
# for (x,y) in dict1.items():
#     print(x,"->",y)
#
# for x in dict1:
#     print(dict1[x])


#Guess game-->

print("number of guesses = 9")
n=18
for i in range(1,10,1) :
 a1=int(input())
 if i==9:
     print("Sorry,you lose")
     break
 if a1>n:
    print("get smaller and guess left=" ,9-i)
 elif a1==n:
    print("congrats! you won",f"and you won by {i} guess")
    break
 else:
    print("get larger and guess left=",9-i)
