import pyinputplus as pyip

values = input("Input some comma seprated numbers : ")
l = values.split(",")
t = tuple(l)
s=len(l)
print("Tuple : ", str(t))
K = pyip.inputNum(prompt='Enter a value of K:',greaterThan=0,max=s)
sc = sorted(list(t))
vals = []
for i in range(K):
    vals.append(sc[i])
for i in range((len(sc) - K), len(sc)):
    vals.append(sc[i])
print("K maximum and minimum values : ", str(vals))
