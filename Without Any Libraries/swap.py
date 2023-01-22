list1 = []
while True:
    try:
        L = input("\nEnter the number of elements in the list: ")
        if L.isnumeric() == False:
            raise ValueError
        L = int(L)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
for i in range(L):
    while True:
        try:
            item = input("\nEnter an element: ")
            if item.isnumeric() == False:
                raise ValueError
            item = int(item)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    list1.append(item)
print(list1)


print("Index 1")
while True:
    ch = int(input("Enter 1 for positive index or 2 for negative index: "))
    if ch == 1:
        pos1 = int(input("Enter index: "))
        if pos1 >= 0 and pos1 < L:
            break
        else:
            print("Invalid input. Please enter a valid index.")
    elif ch == 2:
        pos1 = int(input("Enter index: "))
        if pos1 < 0 and pos1 >= -L:
            pos1 = L + pos1
            break
        else:
            print("Invalid input. Please enter a valid index.")
    else:
        print("Invalid input. Please enter 1 for positive or 2 for negative.")


print("Index 2")
while True:
    c = int(input("Enter 1 for positive index or 2 for negative index: "))
    if c == 1:
        pos2 = int(input("Enter index: "))
        if pos2 >= 0 and pos2 < L:
            break
        else:
            print("Invalid input. Please enter a valid index.")
    elif c == 2:
        pos2 = int(input("Enter index: "))
        if pos2 < 0 and pos2 >= -L:
            pos2 = L + pos2
            break
        else:
            print("Invalid input. Please enter a valid index.")
    else:
        print("Invalid input. Please enter 1 for positive or 2 for negative.")

print("List before swapping:")
print(list1)
list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
print("List after swapping:", list1)
