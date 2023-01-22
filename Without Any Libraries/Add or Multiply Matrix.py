while True:
    try:
        rows = int(input('Enter Number of Rows:'))
        if rows <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number greater than 0.")

while True:
    try:
        cols = int(input('Enter Number of Columns:'))
        if cols <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number greater than 0.")

matrix_A=[]
print("\nEnter the Values for Matrix A")
for i in range(rows):
    r=[]
    for j in range(cols):
        while True:
            try:
                value = input(f"column {j+1} -> Enter {i+1} element: ")
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        r.append(value)
    matrix_A.append(r)

matrix_B=[]
print("\nEnter the Values for Matrix B")
for i in range(rows):
    r=[]
    for j in range(cols):
        while True:
            try:
                value = input(f"column {j+1} -> Enter {i+1} element: ")
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        r.append(value)
    matrix_B.append(r)


print('\nMatrix-A :')
for i in matrix_A:
    print(i)

   
print('\nMatrix-B :')
for i in matrix_B:
    print(i)

result = [[0 for j in range(cols)] for i in range(rows)]

print("\nChoose on operation : \n")
while True:
    print("\nEnter 0 to exit ")
    ch = input("Enter 1 for addition or 2 for multiplication: ")
    if ch == '1':
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix_A[i][j] + matrix_B[i][j]
        print() 
        print('\nAddition of Matrix-A and Matrix-B is :')
        for i in result:
            print(i)
    elif ch == '2':
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix_A[i][j] * matrix_B[i][j]
        print() 
        print('\nMultiplication of Matrix-A and Matrix-B is :')
        for i in result:
            print(i)
    
    elif ch =='0':
        break
    else:
        print("\nWrong Input. Please enter 1 for addition or 2 for multiplication.")
