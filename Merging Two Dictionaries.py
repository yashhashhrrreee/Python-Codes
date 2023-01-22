import pyinputplus as pyip
from collections import defaultdict

def Merge(dict1, dict2): 
   for key, value in dict2.items():
      if key in dict1:
         dict1[key] = [value , dict1[key]]
      else:
         dict1[key]=value  
   return(dict1)

print('------------------------------------------------------------------')
n1= pyip.inputInt(prompt='Enter Size of Dictionary 1 : ',min=0)
stu=[]
l=[]
for i in range(0,n1):
    stu.append(pyip.inputNum("Enter the Key: "))
    stu.append(pyip.inputStr("Enter the Value: "))
    l.append(stu)
    stu = []
d1 = defaultdict(list)
for k, v in l:
    d1[k].append(v)
d1= dict((k1, tuple(v1)) for k1,v1 in d1.items())
print('------------------------------------------------------------------')
print("Dictionary 1:")
for k, v in d1.items():
    print(k, v)

print('------------------------------------------------------------------')
n2= pyip.inputInt(prompt='Enter Size of Dictionary 2 : ',min=0)
st=[]
l1=[]
for i in range(0,n2):
    st.append(pyip.inputNum("Enter the Key: "))
    st.append(pyip.inputStr("Enter the Value: "))
    l1.append(st)
    st = []
d2 = defaultdict(list)
for k1, v1 in l1:
    d2[k1].append(v1)
d2= dict((k1, tuple(v1)) for k1,v1 in d2.items())
print('------------------------------------------------------------------')
print("Dictionary 2:")
for k, v in d2.items():
    print(k, v)

d3 = (Merge(d1, d2)) 
print('------------------------------------------------------------------\n')
print("\nDictionary after merging ::>")
print(d3)
print('------------------------------------------------------------------')
