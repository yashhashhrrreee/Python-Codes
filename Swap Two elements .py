import pyinputplus as pyip
list1 = []
L=pyip.inputInt(prompt="Enter The No of List Elements: ",greaterThan=0)
for i in range(L):
    item = pyip.inputInt(prompt="Enter Elements : ", greaterThan=0)
    list1.append(item)
print(list1)

#pos1=pyip.inputInt(prompt="Enter Index 1 :",max=L,greaterThan=-(L+1),blockRegexes=[r'(-0)'])
#pos2=pyip.inputInt(prompt="Enter Index 2 :",max=L,greaterThan=-(L+1),blockRegexes=[r'(-0)'])

print('Index 1')
while True:
    ch = pyip.inputMenu(['Positive','Negative'], numbered=True)
    if ch=='Positive':
            pos1=pyip.inputInt(prompt="Enter Index :",max=(L-1),min =0,blockRegexes=[r'(-0)'])
            break
    if ch=='Negative':
           pos1=pyip.inputInt(prompt="Enter Index :",max=(-1),min=-(L),blockRegexes=[r'(-0)'])  
           break
           
print('Index 2')
while True:
    c = pyip.inputMenu(['Positive','Negative'], numbered=True)
    if c=='Positive':
        pos2=pyip.inputInt(prompt="Enter Index :",max=(L-1),min =0,blockRegexes=[r'(-0)'])
        break
    if c=='Negative':
        pos2=pyip.inputInt(prompt="Enter Index :",max=(-1),min=-(L),blockRegexes=[r'(-0)'])  
        break
           
        

print("List before swapping:")
print(list1)
list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
print("List after Swapping: ",list1)
