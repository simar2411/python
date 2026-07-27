p1="make a lot of money"
p2="buy noW"
p3="subscribe this"
p4="click this"

message = input("enter your comment")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("this message contain spanm comments")
else:
    print("no spam")