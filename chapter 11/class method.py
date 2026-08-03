class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"this class attribute is {cls.a}")

e = employee()
e.a=45#instance attribute show if decorator used

e.show()