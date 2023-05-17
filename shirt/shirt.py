import sys
from PIL import Image
from PIL import ImageOps
def main():

    try:
        if len(sys.argv[0:])==3:
            iimg_name=sys.argv[1]
            oimg_name=sys.argv[2]
        elif len(sys.argv[0:])<2:
            sys.exit("too few arguments")
        else:
            sys.exit("too many arguments")

    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        if is_valid(iimg_name,oimg_name):
            with Image.open(iimg_name) as iimg :
                shirt = Image.open("shirt.png")
                size = shirt.size
                nf=ImageOps.fit(iimg,size)
                nf.paste(shirt,shirt)
                nf.save(oimg_name)



def is_valid(iimg_name,oimg_name):
    if iimg_name.lower().endswith(".png") and oimg_name.lower().endswith(".png")  :
        return True
    elif iimg_name.lower().endswith(".jpg") and oimg_name.lower().endswith(".jpg")  :
        return True
    elif iimg_name.lower().endswith(".jpeg") and oimg_name.lower().endswith(".jpeg")  :
        return True
    else :
        sys.exit("ivalid input or output")

if __name__=="__main__":
    main()