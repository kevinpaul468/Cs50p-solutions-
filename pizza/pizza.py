import sys
import csv
from tabulate import tabulate

def main():
    table=[]

    try:
        if len(sys.argv)==2:
            file_name=sys.argv[1]
        elif len(sys.argv[0:])<2:
            sys.exit("too few arguments")
        else:
            sys.exit("too many arguments")

    except FileNotFoundError:
        sys.exit(f"No such file or directory: {file_name}")
    else:
         if is_valid(file_name):
             with open(file_name) as file:
                 reader=csv.reader(file)
                 for row in reader:
                     table.append(row)
                 print(tabulate(table[1:],headers=table[0],tablefmt="grid"))
def is_valid(file_name):
    if file_name.endswith(".csv") :
        return True
    else:
        sys.exit("not a csv file")


if __name__=="__main__":
    main()