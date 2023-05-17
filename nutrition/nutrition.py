fruits=["Apple","Avocado","Banana","Cantaloupe","Grapefruit","Grapes","Honeydew Melon","Kiwifruit","Lemon","Lime","Nectarine","Orange","Peach","Pear","Pineapple","Plums","Strawberries","Sweet Cherries","Tangerine","Watermelon"]
cal=[130,50,110,50,60,90,50,90,15,20,60,80,60,100,50,70,50,100,50,80]
x=input("Item: ")
for fruit in fruits:
    if x.upper()==fruit.upper():
        print(cal[fruits.index(fruit)])
        break
