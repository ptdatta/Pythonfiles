import time

# init=time.time()  #current time return
# k=0
# while(k<5):
#     print("hello")
#     time.sleep(2)
#     k+=1
# print(f"while loop run in {time.time()-init} seconds")
#
# init2=time.time()
# for i in range(5):
#     print("hello")
#     time.sleep(2)
# print(f"for loop run in {time.time()-init2} seconds")

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)

b=time.time()
print(b)
i=0
while(i<2):
    print("hello")
    time.sleep(1)
    i+=1
a=time.time()
print(a)
print(a-b)

