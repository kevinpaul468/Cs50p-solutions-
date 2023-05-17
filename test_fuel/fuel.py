def main():
    while True:
        try:
            fraction=input("Fraction: ")
            percentage=convert(fraction)
            if percentage== False:
                continue
            else:
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
    print(gauge(percentage))


def convert(fraction):
    x,y=fraction.split("/")
    x=int(x)
    y=int(y)
    percentage=round(float(x/y)*100)
    if percentage >100:
        return False
    else :
        return percentage


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()