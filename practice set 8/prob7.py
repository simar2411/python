l=["harry","rohan","shubham","an"]
def rem(l, Word):
    n=[]

    for item in l:
        if not(item == Word):
            n.append(item.strip(Word))
    return n

print(rem(l,"an"))