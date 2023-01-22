def get_sum(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total

arr = input("Enter a list of values: ").split()

for i in range(len(arr)):
    while not arr[i].isnumeric():
        arr[i] = input("Enter an integer value for index " + str(i) + ": ")

print("Array ", arr)
print("Sum of the array:",get_sum(arr))
