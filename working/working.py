import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches=re.search(r"^(\d?\d(?:\:\d\d)?) (AM|PM) to (\d?\d(?:\:\d\d)?) (AM|PM)$",s)
    if matches==None:
        raise ValueError
    time1,suf1,time2,suf2=matches.groups()
    hours1,mins1=get_verified_time(time1)
    hours2,mins2=get_verified_time(time2)
    time1=twele_to_twenty_four(hours1,suf1,mins1)
    time2=twele_to_twenty_four(hours2,suf2,mins2)
    return f"{time1} to {time2}"



def get_verified_time(time):
    if ":" in time :
        hours,minutes=time.split(":")
        hours=int(hours)
        minutes=int(minutes)
    else :
        hours=int(time)
        minutes=0

    if hours> 12 or minutes>59 :
        raise ValueError
    else:
        return hours,minutes






def twele_to_twenty_four(hours,suf,mins="o"):
    if hours==12 and suf=="AM":
        return f"00:{mins:02}"
    elif hours==12 and suf=="PM":
        return f"{hours:02}:{mins:02}"
    elif suf =="PM" :
        return f"{hours+12 :02}:{mins:02}"
    else:
        return f"{hours:02}:{mins:02}"


if __name__ == "__main__":
    main()