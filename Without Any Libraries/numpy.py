import numpy as np

# Creating an array
while True:
    array_input = input("Enter the elements of the array separated by spaces: ")
    if array_input.strip() == "":
        print("Array cannot be blank.")
        continue
    try:
        array = np.array(list(map(int, array_input.split())))
        break
    except ValueError:
        print("Array elements can only be numeric.")

print("\nArray:")
print(array)

# Array shape
print("\nArray shape:")
print(np.shape(array))

# Array reshape
while True:
    reshape_input = input("\nEnter the new shape of the array (rows columns): ")
    if reshape_input.strip() == "":
        print("New shape cannot be blank.")
        continue
    try:
        rows, columns = map(int, reshape_input.split())
        reshaped_array = np.reshape(array, (rows, columns))
        break
    except ValueError:
        print("New shape can only be numeric.")

print("\nReshaped Array:")
print(reshaped_array)

# Array transpose
print("\nArray transpose:")
print(np.transpose(array))

# Array flattening
print("\nArray flattening:")
print(np.ravel(array))

# Array addition
while True:
    add_input = input("\nEnter the value to add to the array: ")
    if add_input.strip() == "":
        print("Value cannot be blank.")
        continue
    if not add_input.isnumeric():
        print("Value can only be numeric.")
        continue
