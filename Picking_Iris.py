import requests
import pickle

r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
d=r.text.split("\n")
c=[item.split(",") for item in d]
file="Iris.pkl"
fileobj=open(file,'wb')
pickle.dump(c,fileobj)
fileobj.close()

file = "Iris.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)