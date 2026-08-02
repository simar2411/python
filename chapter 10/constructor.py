class employee:
    #name="simar"
    language="py"
    salary=10000


    def __init__(self, name, salary, language):#dunder method Which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creting an object")


    def getinfo(self):
        print(f"salary is {self.salary} and language is {self.language}")


    @staticmethod  #decorator self nhi lega no object
    def greet():
        print("hello good morning")

simar=employee("simar",1200000,"javascript")
#simar.name="simar"
print(simar.salary,simar.language,simar.name)
