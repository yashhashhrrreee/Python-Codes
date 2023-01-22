def merge_dicts(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in result:
            result[key] += ' ,' + value
        else:
            result[key] = value
    for key, value in dict2.items():
        if key in result:
            result[key] += ' ,' + value
        else:
            result[key] = value
    return result

print("\nEnter Data for dictionary 1:\n")
d1 = {}

while True:
    key = input("Enter a key (Enter '-0' to quit): ")
    if key == '-0':
        break
    elif key.strip() == "": # check if key is not empty
        print("Key cannot be blank. Please enter a valid key.")
        continue
    value = input("Enter a value: ")
    if value.strip() == "": # check if key is not empty
        print("Value cannot be blank. Please enter a valid Value.")
        continue
    if key in d1:
        d1[key] += ' ,' + value
    else:
        d1[key] = value

for key, values in d1.items():
    print(f"{key}: {values}")

print("  ")

print("\nEnter Data for dictionary 2:\n")
d = {}

while True:
    key = input("Enter a key (Enter '-0' to quit): ")
    if key == '-0':
        break
    elif key.strip() == "": # check if key is not empty
        print("Key cannot be blank. Please enter a valid key.")
        continue
    value = input("Enter a value: ")
    if value.strip() == "": # check if key is not empty
        print("Value cannot be blank. Please enter a valid Value.")
        continue
    if key in d:
        d[key] += ' ,' + value
    else:
        d[key] = value

for key, values in d.items():
    print(f"{key}: {values}")
print("  ")


merged_dict = merge_dicts(d1, d)
print(merged_dict)
