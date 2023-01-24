# calendar->used in case we are working with calendars
# random->used for generating random numbers within certain defined limits
# enum->used while working with enumeration class
# html->for handling and manipulating code in HTML
# math->for working with math functions such as sin, cos, etc.
# runpy->runpy is an important module as it locates and runs python modules without importing them first

import random

# random_number = random.randint(0, 10)    #generates int from 0 to 10
# print(random_number)
rand = random.random() * 100    #generates float numbers from o to 100
print(rand)
# lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
# choice = random.choice(lst)
# print(choice)


# Snake,Water,Gun
# game=["Snake","Water","Gun"]
# me=0
# com=0
# i=0
# while(i<10):
#     cc=random.choice(game)
#     mec=input()
#     d=mec.capitalize()
#     if(cc=="Snake" and d=="Gun" or cc=="Water" and d=="Snake" or cc=="Gun" and d=="Water" ):
#         me+=1
#         print(f"Your points {me} and computer point {com}")
#     else:
#         com+=1
#         print(f"Your points {me} and computer points {com}")
#     i+=1
# if(me>com):
#     print(f"You won by {me-com} points")
# elif(me==com):
#     print("Match drow")
# else:
#     print(f"You lose by {com-me} points")
#



