import sys

def main():
    try:
        if len(sys.argv[0:])==2:
            file_name=sys.argv[1]
        elif len(sys.argv[0:])<2:
            sys.exit("too few arguments")
        else:
            sys.exit("too many arguments")
        if is_valid(file_name):
            file=open(file_name)


    except FileNotFoundError:
        sys.exit(f"No such file or directory: {file_name}")
    else:
        lines=0
        for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.lstrip()=="":
                    continue
                else:
                    lines +=1
        print(f"lines: {lines}")
        close(file)
def is_valid(file_name):
    if file_name.endswith(".py") :
        return True
    else:
        sys.exit("not a python file")


if __name__=="__main__":
    main()