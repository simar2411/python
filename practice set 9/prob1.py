f=open("poem.txt")
c=f.read()
if ("twinkle" in c):
    print("Twinkle is present")
else:
    print("not present")
f.close()