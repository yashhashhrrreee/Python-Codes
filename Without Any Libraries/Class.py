class Employee:
    id_set = set()
    def __init__(self):
        self.id=0
        self.name=""
        self.gender=""
        self.city=""
        self.salary=0
    def setData(self):
        while True:
            id_input = input("Enter ID: \t")
            if id_input.strip() == "":
                print("ID cannot be blank.")
                continue
            if not id_input.isnumeric():
                print("ID can only be numbers.")
                continue
            if int(id_input) in Employee.id_set:
                print("ID already exists.")
                continue
            self.id = int(id_input)
            Employee.id_set.add(int(id_input))
            break
        while True:
            name_input = input("Enter Name \t")
            if name_input.strip() == "":
                print("Name cannot be blank.")
                continue
            if name_input.isnumeric():
                print("Name can not be numeric.")
                continue
            self.name = name_input
            break
        while True:
            print("Enter Gender:")
            print("1. Male")
            print("2. Female")
            print("3. Other")
            gender_input = input()
            if gender_input not in ["1","2","3"]:
                print("Invalid Input")
                continue
            if gender_input == "1":
                self.gender = "Male"
            elif gender_input == "2":
                self.gender = "Female"
            else:
                self.gender = "Other"
            break
        while True:
            city_input = input("Enter City \t")
            if city_input.strip() == "":
                print("City cannot be blank.")
                continue
            if city_input.isnumeric():
                print("City can not be numeric.")
                continue
            self.city = city_input
            break
        while True:
            salary_input = input("Enter Salary: \t")
            if salary_input.strip() == "":
                print("Salary cannot be blank.")
                continue
            if not salary_input.isnumeric():
                print("Salary can only be numbers.")
                continue
            self.salary = int(salary_input)
            break

    def showData(self):
        print("--------------------------------------------")
        print("Id\t:",self.id)
        print("Name\t:", self.name)
        print("Gender\t:", self.gender)
        print("City\t:", self.city)
        print("Salary\t:", self.salary)
        print("--------------------------------------------")
            
while True:
    n_input = input("Enter The No of List Elements: ")
    if n_input.strip() == "":
        print("Number of elements cannot be blank.")
        continue
    if not n_input.isnumeric():
        print("It can only be numbers")
        continue
    else:
        n = int(n_input)
    break

class_list = []
for i in range(n):
    class_list.append(Employee())
    class_list[i].setData()

for i in range(n):
    class_list[i].showData()

