items={}
while True:
    try :
        item=input()
        if item in items :
            items[item]+=1
        else:
            items[item]=1

    except EOFError:
        break

for i in sorted(items.keys()):
    print(f"{items[i]} {i.upper()}")
