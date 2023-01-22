import pyinputplus as pyip

str = pyip.inputStr(prompt="Enter String:")
while True:
    print("-----------------------------------------------------------------------")
    print("    ")
    ch=pyip.inputMenu(['To Change The Initial String', 
                       'To Copy String To Another String', 
                       'To Concat String To Another String',
                       'To Find Length Of The String',
                       'To Reverse The String',
                       'To Exit'],numbered=True)
    print("-----------------------------------------------------------------------")
    print("    ")

    if ch=='To Change The Initial String':
            str = pyip.inputStr(prompt="Enter New String:")
            print(str)
            continue
            print("    ")
    if ch=='To Copy String To Another String':
            cpy=str
            print("Copied String is",cpy)
            print("    ")
    if ch=='To Concat String To Another String':
            con=pyip.inputStr(prompt="Enter 2nd String:")
            print(str+" "+con) 
            print("    ")
    if ch=='To Find Length Of The String':
            count = 0
            for i in str:
                count+=1
            print('Length Of String = ',count)
            print("    ")
    if ch=='To Reverse The String':
            count = 0
            for t in str:
                count+=1
            print('Printing Reversed String....')
            t=count
            t-=1
            rev=''
            for i in range(count):
                rev=rev+str[t]
                t-=1
            print(rev)  
            print("    ")    
    if ch=='To Exit':
            break
    else:
            continue



