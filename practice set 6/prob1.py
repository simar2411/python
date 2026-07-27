a=int(input("enter number 1 :"))
b=int(input("enter number 2 :"))
c=int(input("enter number 3 :"))
d=int(input("enter number 4 :"))

if(a>b and a>c and a>d):
    print("a is the greatest number")
elif(b>c and b>d):
    print("b is the greatest number")
elif(c>d):
    print("c is the greatest number")
else:
    print("d is the greatest number")

print("end of code")