d={}#empty dictionary
marks={
    "harry":100,
    "shubham":56,
    "rohan":32
}
print(marks)
print(type(marks))
print(marks["harry"])#same as get key but error

print(marks.items())#tuple forms 
print(marks.keys())
print(marks.values())
marks.update({"harry":99 , "renuka":91})#can also add up the values here
print(marks)

print(marks.get("shalu"))#no error if key not match
#returns none

print(marks.pop("rohan"))
print(marks.popitem())