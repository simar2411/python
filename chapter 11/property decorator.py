class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"this class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"


    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e = employee()
e.a=45#instance attribute show if decorator used
e.name="simar kaur"
print(e.fname,e.lname)
 

e.show()