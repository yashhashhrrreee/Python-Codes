# Program to add and multiply two matrices using nested loop
import pyinputplus as pyip

rows = pyip.inputInt(prompt='Enter Number of Rows:',greaterThan=0)
cols  = pyip.inputInt(prompt='Enter Number of Columns:',greaterThan=0)
 

matrix_A=[]
print("Enter the Values for Matrix B")
for i in range(rows):
   r=[]
   for j in range(cols):
      r.append(pyip.inputNum(prompt=f"column {j+1} -> ENter {i+1} element:")) 
   matrix_A.append(r)


matrix_B=[]
print("Enter the Values for Matrix B")
for i in range(rows):
   r=[]
   for j in range(cols):
      r.append(pyip.inputInt(prompt=f"column {j+1} -> ENter {i+1} element:")) 
   matrix_B.append(r)



print('Matrix-A :')
for i in matrix_A:
   print(i)

   
print('Matrix-B :')
for i in matrix_B:
     print(i)

result = [[0 for j in range(cols)] for i in range(rows)]

print("Choose on operation : \n")
ch = pyip.inputMenu(['Addition','Multiplication'], numbered=True)
if ch=="Addition":
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] + matrix_B[i][j]
    print() 
    print('Addition of Matrix-A and Matrix-B is :')
    for i in result:
      print(i)

elif ch=="Multiplication":
   for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] * matrix_B[i][j]
   print() 
   print('Multiplication of Matrix-A and Matrix-B is :')
   for i in result:
     print(i)

else:
   print("Wrong Input")