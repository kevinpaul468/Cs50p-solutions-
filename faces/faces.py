def convert(x) :
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

x=input()
x=convert(x)
print(x)