with open("this.txt","r") as f:
    content1=f.read()

with open("this copy.txt","r") as f:
    content2=f.read()

if content1==content2:
    print("both files are same")
else:
    print("both files are not same")