from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

arg= sys.argv[1:]

if arg==[]:
    s=input("Input: ")
    f=random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif (arg[0]=="-f" or arg[0]=="--font")and arg[1] in figlet.getFonts():
    s=input("Input: ")
    f=arg[1]
    figlet.setFont(font=f)
    print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")



