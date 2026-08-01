Word=["donkey","dumb","stupid","ugly","bad"]

with open("file.txt","r") as f:
    content=f.read()

for word in Word:
    contentnew=content.replace(word,"#"*len(word))

with open("file.txt","w") as f:
    f.write(contentnew)