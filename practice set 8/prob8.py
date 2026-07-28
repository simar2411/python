#multiplication number
n=int(input("enter number : "))
def table(n):
    for i in range (1,11):
        print(n ,"X",i , "=",n*i)

print(table(n))