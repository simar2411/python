class employee:
#parent class
    company = "ITC"
    name = "default name"
    salary = 50000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder:
    language="python"
    def printlanguages(self):
        print(f"out of all your langugae is : {self.language}")

class programmer(employee , coder):
    company="ITC infotech"

    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language ")

a=employee()
b=coder()
c=programmer()

print(c.company,c.language)

c.show()
c.printlanguages()
c.showlanguage()