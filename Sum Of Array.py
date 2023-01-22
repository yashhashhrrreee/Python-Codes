sum=0
arr=input("Enter Array Elements : ").split()
for i in range(len(arr)):
    try:
        n=int(arr[i])
        sum = sum + n
    except ValueError:
        print('The Character Detected is  is  \n',arr[i])
        while True:
            n=input('Press 0 to ignore \nPress 1 to Edit the element : ')
            try:
                if int(n)==1:
                    new=input('Enter new element : ')
                    sum = sum + int(new)
                    break
                if int(n)==0:
                    break   
            except:
                    print('Wrong Input Enter Again')         
        
print('Sum Of Array = ',sum)