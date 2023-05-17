s=input("Expression: ")
x,y,z=s.split(" ")
x=int(x)
z=int(z)
if y=="+":
    print(float(x+z))
if y=="-":
    print(float(x-z))
if y=="*":
    print(float(x*z))
if y=="/":
    print(float(x/z))
