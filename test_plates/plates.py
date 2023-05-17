
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len_check(s) and num_nd_pun_check(s):
        return True
    else :
        return False

def num_nd_pun_check(s):
    x=len(s)
    if s.isalpha():
        return True
    for i in s :
        if i.isnumeric():
            x= s.index(i)
            break
    if s[x]=="0":
        return False

    if s[x:].isnumeric():
        if s[0:x].isalpha():
            return True



def len_check(s):
    if len(s)<=6 and len(s)>=2:
        return True


if __name__=="__main__":
    main()