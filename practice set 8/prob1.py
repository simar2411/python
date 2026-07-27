'''def greatest():
    n1=int(input("enter number : "))
    n2=int(input("enter number : "))
    n3=int(input("enter number : "))
    if(n1>n2 and n1>n3):
        print("greatest",n1)
    elif(n2>n3):
        print("greatest",n2)
    else:
        print("greates",n3)

greatest()'''


a=int(input("enter number :"))
b=int(input("enter number :"))
c=int(input("enter number :"))
def greatest(a,b,c):
    if(a>b and a>c):
        print("greatest",a)
    elif(b>c):
        print("greatest",b)
    else:
        print("greatest",c)

greatest(a,b,c)

