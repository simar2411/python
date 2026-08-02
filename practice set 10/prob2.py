class calculator:
    def square(self,x):
        return x*x

    def cube(self,x):
        return x*x*x

    def squareroot(self,x):
        return x**0.5


c=calculator()
print(c.square(4),c.cube(4),c.squareroot(4))


'''class calculator2:
    def __init__(self,x):
        self.x=x

    def square(self):
        return self.x*self.x

    def cube(self):
        return self.x*self.x*self.x

    def squareroot(self):
        return self.x**0.5'''
  