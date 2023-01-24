import  random
names=["Rohan Das","Shubham Agarwal","Ritesh Arora"]
list=[]
for i in names:
    list.append(i.split())

list2=[i[1] for i in list]
for i in list:
    i[1]=random.choice(list2)

newnames=[]
for i in range(3):
    newnames.append(list[i][0] +" "+ list[i][1])

print(newnames)