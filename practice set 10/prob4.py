class calculator:
    def square(self,x):
        return x*x

    def cube(self,x):
        return x*x*x

    def squareroot(self,x):
        return x**0.5

@staticmethod 
def greet():
    print("hello user")

greet()
c=calculator()
print(c.square(4),c.cube(4),c.squareroot(4))

