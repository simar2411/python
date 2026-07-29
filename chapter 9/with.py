f=open("file.txt")
print(f.read())
f.close()

#same written as with statement:

with open("files.txt" )as f:
    print(f.read())

#no need to close the file