months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try :
        date=input("Date: ")
        x,y,z= date.split("/")
        x=x.strip(" ")
        z=z.strip(" ~")
        x=int(x)
        y=int(y)
        if x>12 or x<1:
            continue
        if y>31:
            continue
        x=str(x)
        y=str(y)
        break
    except ValueError:
        try:
            x,y,z=date.split(" ")
            if y.endswith(","):
                y=y.strip(",")
            else:
                continue
            x=months.index(x) +1
            if x>12 or x<1:
                continue
            y=int(y)
            if y>31:
                continue
            y=str(y)
            x=str(x)
            break
        except :
            pass
print (f"{z}-{x.zfill(2)}-{y.zfill(2)}")
