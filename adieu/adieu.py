import inflect
p = inflect.engine()
x=[]
while True:
    try :
        name=input("Name: ")
        x.append(name)
    except EOFError :
        break
print(f"Adieu, adieu, to {p.join(x)}")
