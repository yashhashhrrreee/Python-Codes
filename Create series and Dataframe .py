import pyinputplus as pyip
import pandas as pd

def list(list1):
    l=pyip.inputInt(prompt="Enter The No of List Elements: ",min=0)
    for i in range(l):
        item = pyip.inputInt(prompt="Enter Elements : ",min=0)
        list1.append(item)
    print(list1)

def array(arr):
    number = pyip.inputInt(prompt="Enter The No of Elements: ",greaterthan=0)
    for i in range(int(number)): 
        n = pyip.inputInt(prompt="Enter Number in Array : ",greaterthan=0)
        arr.append(int(n)) 
    print ('ARRAY: ',arr) 

def dictionary(n):
    d = {}
    for i in range(n):
        keys = pyip.inputInt("Enter the Key :")
        values = pyip.inputStr("Enter the Value:")
        d[keys] = values
    print(d)
    dframe = pd.DataFrame(d)  
    print(dframe)


while True:
    print("Create : \n")
    ch = pyip.inputMenu(['Series','Dataframe',], numbered=True)
    if ch=="Series":
        list1 = []
        list(list1)
        myvar = pd.Series(list1)
        print(myvar)
    while True:
        if ch=="Dataframe":
            print("Create Data-Frame using : \n")
            c = pyip.inputMenu(['List','Array','Dictionary'], numbered=True)
            if c=="List":
                list1 = []
                list(list1)
                dframe = pd.DataFrame(list1)  
                print(dframe)
            if c=="Array":
                arr =[]
                array(arr)
                dframe = pd.DataFrame(arr)  
                print(dframe)
            if c=="Dictionary":
               n= pyip.inputInt(prompt='Enter The no of inputs In Dictionary :')
               dictionary(n)
            else:
                break
        else:
            break

