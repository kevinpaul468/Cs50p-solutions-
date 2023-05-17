while True:
    try:
        fraction=input("Fraction: ")
        x,y=fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y:
            continue
        fraction=round(float(x/y)*100)
        break
    except ZeroDivisionError :
        pass
    except ValueError:
        pass

if fraction<=1:
    print("E")
elif fraction>=99:
    print("F")
else:
    print(f"{fraction}%")