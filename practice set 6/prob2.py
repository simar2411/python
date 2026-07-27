sub1=int(input("enter marks 1 :"))
sub2=int(input("enter marks 2 :"))
sub3=int(input("enter marks 3 :"))

percentage=(sub1+sub2+sub3)*100/300

if (percentage>=40 and sub1>33 and sub2>33 and sub3>33):
    print("you are pass",percentage)
else:
    print("you failed",percentage)   

 