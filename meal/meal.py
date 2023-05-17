def main():
    time=input("What time is it? ")
    time = convert(time)
    if (time>=7 and time<=8) :
        print("breakfast time")

    if (time>=12 and time<=13) :
        print("lunch time")

    if (time>=18 and time<=19) :
        print("dinner time")


def convert(time):
    h,m=time.split(":")
    h=int(h)
    m=int(m)
    return h+(m/60)


if __name__ == "__main__":
    main()