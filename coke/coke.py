x=0
while x<50 :
    print("Amount Due:",+(50-x))
    y=int(input("Insert Coin: "))
    if y==5 or y==10 or y==25 :
        x=x+y
print("Change Owed:",+(x-50))