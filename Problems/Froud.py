import  random

def rohanmultiplication(number):
    wrong=random.randint(0,9)
    table=[i * number for i in range(1,11)]
    table[wrong]=table[wrong] + random.randint(0,10)
    return table;

def iscorrect(table,number):
    for i in range(10):
        if(table[i]!=(i+1)*number):
            print(f"{i} is the wrong index,right multiplication is {i*number}")
    return None

if __name__ == '__main__':
    n=random.randint(0,100)
    list=rohanmultiplication(n)
    print(list)
    iscorrect(list,n)