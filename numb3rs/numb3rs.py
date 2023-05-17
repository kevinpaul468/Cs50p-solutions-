import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip=re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip)

        for i in range(1,5):
            if int(ip.group(i)) <0 or int(ip.group(i)) >255 :
                return False
        return True
    except AttributeError:
        return False

...


if __name__ == "__main__":
    main()