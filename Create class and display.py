import pyinputplus as pyip

class Employee:
    id=0
    name=""
    gender=""
    city=""
    salary=0
    def setData(self):
            self.id=pyip.inputInt(prompt="Enter ID: \t",blockRegexes=[r'(-0)'])
            self.name = pyip.inputStr(prompt="Enter Name \t")
            self.gender =pyip.inputMenu(['Male','Female','Other',],numbered=True)
            self.city = pyip.inputStr(prompt="Enter City \t")
            self.salary=pyip.inputInt(prompt="Enter Salary: \t",blockRegexes=[r'(-0)'])    
            print(' ')
    def showData(self):
            print("--------------------------------------------")
            print("Id\t:",self.id)
            print("Name\t:", self.name)
            print("Gender\t:", self.gender)
            print("City\t:", self.city)
            print("Salary\t:", self.salary)
            print("--------------------------------------------")
        
            
n=pyip.inputInt(prompt="Enter The No of List Elements: ",greaterThan=0,blockRegexes=[r'(-0)'])

class_list = []
for i in range(n):
    class_list.append(Employee())
    # class_list[i] = Employee()
    class_list[i].setData()

for i in range(n):
    class_list[i].showData()
