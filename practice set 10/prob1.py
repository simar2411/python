class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p = programmer("roni",100000,1234)
print(p.name,p.salary,p.pin,p.company)

m = programmer("moni",130000,12349)
print(m.name,m.salary,m.pin,m.company)