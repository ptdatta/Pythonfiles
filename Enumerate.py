# list_1=["code","with","harry"]
# for index,val in enumerate(list_1):
#     print(index,val)
#

# list_2 = ["Python", "Programming", "Is", "Fun"]
# #Counter value starts from 5
# result = enumerate(list_2, 3)
# print(list(result))


l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Jarvis please buy {item}")

# for i in range(0,4,1):
#     if(i%2==0):
#         print(f"Jarvis please buy {l1[i]}")



