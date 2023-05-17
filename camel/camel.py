s=input("camelCase: ")
for i in range (len(s)):
    if s[i].upper() ==s[i]:
        x,y= s.split(s[i]cd)
        s=x+"_"+s[i].lower()+y
print(s)
