result = lambda n1, n2, n3: n1 + n2 + n3
print ("Sum of three values : ", result( 10, 20, 25 ))

# same as
# def result(n1,n2,n3):
#     return n1+n2+n3




a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)
