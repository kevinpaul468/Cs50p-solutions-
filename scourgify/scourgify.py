import sys
import csv
def main():
    names=[]
    house=[]
    first=[]
    last=[]
    try:
        if len(sys.argv[0:])==3:
            rfile_name=sys.argv[1]
            wfile_name=sys.argv[2]

        elif len(sys.argv[0:])<2:
            sys.exit("too few arguments")
        else:
            sys.exit("too many arguments")
        if is_valid(rfile_name):
             with open(rfile_name) as rfile:
                 reader=csv.DictReader(rfile)
                 for row in  reader:
                     names.append(row['name'])
                     house.append(row['house'])
                 for name in names:
                     la,fi=name.split(",")
                     last.append(la.strip())
                     first.append(fi.strip())
             with open(wfile_name,"w") as wfile:
                 fieldnames=['first','last','house']
                 writer=csv.DictWriter(wfile,fieldnames=fieldnames)
                 writer.writeheader()

                 for _ in range(0,len(house)):
                     writer.writerow( {'first':first[_], 'last':last[_], 'house':house[_]} )

    except FileNotFoundError:
        sys.exit(f"No such file or directory: {rfile_name}")

def is_valid(file_name):
    if file_name.endswith(".csv") :
        return True
    else:
        sys.exit("not a csv file")


if __name__=="__main__":
    main()