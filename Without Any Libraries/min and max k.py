arr = input("Enter values: ").split()

for i in range(len(arr)):
    while not arr[i].isnumeric():
        arr[i] = input("Enter an integer value for index " + str(i) + ": ")

tup = tuple(map(int,arr))
print(tup)
s=len(arr)
while True:
    K = input("Enter a value of K: ")
    if not K.isdigit() or int(K) <= 0 or int(K) > s:
        if not K.isdigit():
            print("Only digits are allowed.")
        elif int(K) <= 0:
            print("K should be greater than 0")
        else:
            print("K should be less than or equal to number of elements in the tuple.")
    else:
        break

sc = sorted(list(tup))
vals =[]
for i in range(int(K)):
    vals.append(sc[i])
for i in range((len(sc) - int(K)), len(sc)):
    vals.append(sc[i])
print("K maximum and minimum values : ", str(vals))