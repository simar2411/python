'''
***
**
*
'''
n=int(input("enter number: "))
def pattern(n):
    for i in range(n,0,-1):
        print("*"*i)

pattern(n)

'''
if(n==0):
    return 
print("*"*n)
pattern(n-1)   
 
'''