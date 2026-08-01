class employee:
    #name="simar"
    language="py"
    salary=10000

simar=employee()
simar.name="simar"#instance attribute
print(simar.salary,simar.language)



rohan=employee()
rohan.name="rohan kika"
print(rohan.language,rohan.salary)

print(rohan.name,simar.name)

#name is object attribute and salary and language attributes as they directly belong to the class