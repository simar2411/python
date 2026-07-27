n=int(input("enter number : "))
i=1 
factorial=1
while(i<=n):
    factorial*=i
    i+=1   
print(factorial)


#or 

number=int(input("enter number : "))
product=1
for i in range(1,number+1):
    product=product*i
print(product)