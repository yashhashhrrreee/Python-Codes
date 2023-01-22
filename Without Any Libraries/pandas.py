import pandas as pd

# Creating a DataFrame
while True:
    rows_input = input("Enter the number of rows in the DataFrame: ")
    if rows_input.strip() == "":
        print("Number of rows cannot be blank.")
        continue
    if not rows_input.isnumeric():
        print("Number of rows can only be numeric.")
        continue
    rows = int(rows_input)
    break

data = {'Name': [], 'Age': [], 'Gender': []}
for i in range(rows):
    while True:
        name_input = input(f"Enter the name of person {i+1}: ")
        if name_input.strip() == "":
            print("Name cannot be blank.")
            continue
        if name_input.isnumeric():
            print("Name can not be numeric.")
            continue
        data['Name'].append(name_input)
        break
    while True:
        age_input = input(f"Enter the age of person {i+1}: ")
        if age_input.strip() == "":
            print("Age cannot be blank.")
            continue
        if not age_input.isnumeric():
            print("Age can only be numeric.")
            continue
        data['Age'].append(int(age_input))
        break
    while True:
        gender_input = input(f"Enter the gender of person {i+1} (Male/Female): ")
        if gender_input.strip() == "":
            print("Gender cannot be blank.")
            continue
        if gender_input.lower() not in ["male", "female"]:
            print("Invalid gender. Please enter 'Male' or 'Female'.")
            continue
        data['Gender'].append(gender_input)
        break

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Accessing the DataFrame
while True:
    column_name = input("\nEnter the name of the column you want to access: ")
    if column_name.strip() == "":
        print("Column name cannot be blank.")
        continue
    if column_name not in df.columns:
        print("Invalid column name. Please enter a valid column name.")
        continue
    break
print("\nColumn:")
print(df[column_name])

# Sorting the DataFrame
while True:
    sort_by = input("\nEnter the name of the column you want to sort the DataFrame by: ")
    if sort_by.strip() == "":
        print("Column name cannot be blank.")
        continue
    if sort_by not in df.columns:
        print("Invalid column name. Please enter a valid column name.")
        continue
    break
df.sort_values(by=sort_by, inplace=True)
print("\nSorted DataFrame:")
print(df)

# Filtering the DataFrame
while True:
    filter_column = input("\nEnter the name of the column you want to filter the DataFrame by: ")
    if filter_column.strip() == "":
        print("Column name cannot be blank.")
        continue
    if filter_column not in df.columns:
        print("Invalid column name. Please enter a valid column name.")
        continue
    break

while True:
    filter_value = input("\nEnter the value you want to filter by: ")
    if filter_value.strip() == "":
        print("Filter value cannot be blank.")
        continue
    break

filtered_df = df[df[filter_column] == filter_value]
print("\nFiltered DataFrame:")
print(filtered_df)

# Grouping the DataFrame
while True:
    group_by = input("\nEnter the name of the column you want to group the DataFrame by: ")
    if group_by.strip() == "":
        print("Column name cannot be blank.")
        continue
    if group_by not in df.columns:
        print("Invalid column name. Please enter a valid column name.")
        continue
    break

grouped_df = df.groupby(group_by).mean()
print("\nGrouped DataFrame:")
print(grouped_df)

