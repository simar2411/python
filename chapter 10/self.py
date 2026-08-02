class employee:
    #name="simar"
    language="py"
    salary=10000


    def getinfo(self):
        print(f"salary is {self.salary} and language is {self.language}")


    @staticmethod  #decorator self nhi lega no object
    def greet():
        print("hello good morning")

simar=employee()
simar.language="javascript"#instance attribute

simar.greet()
print(simar.salary,simar.language)

#simar.getinfo()

employee.getinfo(simar)

