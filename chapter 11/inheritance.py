class employee:
#parent class
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

'''class programmer:
    company = "ITC infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")'''
#inherited class
class programmer(employee):
    company="ITC infotech"

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")
a=employee()
b=programmer()

print(a.company,b.company)