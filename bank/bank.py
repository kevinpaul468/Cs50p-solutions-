g=input("Greeting: ")
g=g.strip()
g=g.lower()
if g.startswith("hello"):
    print("$0")
elif g.startswith("h"):
    print("$20")
else:
    print("$100")