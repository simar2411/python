class employee:
#parent class
    company = "ITC"
    name = "default name"
    salary = 50000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class programmer(employee):
    company="ITC infotech"

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")

class coder(programmer):
    language="python"
    def printlanguages(self):
        print(f"out of all {self.language},{self.name},{self.salary},{self.company}")


c=coder()
c.show()
c.showlanguage()
c.printlanguages()