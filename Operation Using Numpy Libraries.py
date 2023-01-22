import pyinputplus as pyip
from scipy import stats
import numpy as np

def mode(lst):
    freq = {}
    for i in lst:
        freq.setdefault(i, 0)
        freq[i] += 1
    hf = max(freq.values())
    hflst = []
    for i, j in freq.items():
        if j == hf:
            hflst.append(i)
             
    return hflst


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)


print("Array :")
a=pyip.inputInt(prompt="Size of Array: ",greaterThan=0,blockRegexes=[r'(-0)'])
arr = []
for i in range(a):
    arr.append(float(input("Element:")))
arr = np.array(arr)
print(np.floor(arr))


m1=[]
rows = pyip.inputInt(prompt='Enter Number of Rows:',greaterThan=0,blockRegexes=[r'(-0)'])
cols  = pyip.inputInt(prompt='Enter Number of Columns:',greaterThan=0,blockRegexes=[r'(-0)'])

print('\n Matrix')
print("Enter the Values for Matrix ")
for i in range(rows):
   r=[]
   for j in range(cols):
      r.append(pyip.inputNum(prompt=f"column {j+1} -> ENter {i+1} element:")) 
   m1.append(r)
for i in m1:
     print(i)

# creation of matrics
# square root of matrics
# square of matrics
# unique elements in array
# statistic basic


while True :
    print("\nSelect :\n")
    n=pyip.inputMenu(['Array','Matrix','Exit'],numbered=True)
    if n=='Array':
        c = pyip.inputMenu(['Square Root','Square',
                            'Unique Number',
                            'Statistical operations'],numbered=True)
        if c=='Square Root':
            print('\n Square root of the array is:')
            print(np.sqrt(arr))
        if c=='Square':
           print('\nSquare the array:')
           print(np.square(arr))
        if c=='Unique Number':
           print('\nUnique Number in array is:')
           unique(arr)
        if c=='Statistical operations':
           ch=pyip.inputMenu(['Mean','Median','Mode','Standarad Deviation'],numbered=True)
           if ch=='Mean':
             print('\nMean in Array is:')
             print(np.mean(arr))
           if ch=='Median':
             print('\nMedian in Array is:')
             print(np.median(arr))
           if ch=='Mode':
             print('\nMode in Array is:')
             print(mode(arr))
           if ch=='Standarad Deviation':
             print('\nStandarad Deviation of Array is:')
             print(np.std(arr))
           else:
             continue
        else:
            continue
    if n=='Matrix':
        c = pyip.inputMenu(['Square Root','Square',
                           'Unique Number',
                           'Statistical operations'],
                            numbered=True)
        if c=='Square Root':
            print('\n Square root of the Matrix is:')
            print(np.sqrt(m1))
        if c=='Square':
           print('\nSquare the Matrix:')
           print(np.square(m1))
        if c=='Unique Number':
           res = list(set(i for j in m1 for i in j))
           print ("Unique values in matrix are : " + str(res))
        if c=='Statistical operations':
           a = pyip.inputInt(prompt='Enter Number of Axix:',min=0,blockRegexes=[r'(-0)'])
           ch=pyip.inputMenu(['Mean','Median','Mode','Standarad Deviation'],numbered=True)
           if ch=='Mean':
             print('\nMean in Matrix is:')
             print(np.mean(m1))
           if ch=='Median':
             print('\nMedian in Matrix is:')
             print(np.median(m1))
           if ch=='Mode':
             print('\nMode in Matrix is:')
             print(stats.mode(m1, keepdims=True))
           if ch=='Standarad Deviation':
             print('\nStandarad Deviation of Matrix is:')
             print(np.std(m1))
           else:
             continue
        else:
            continue
    if n=='Exit':
      break
    
