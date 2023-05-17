import random


def main():
    score=0
    level=get_level()
    for i in range(1,11):
        x=generate_integer(level)
        y=generate_integer(level)
        for i in range(1,4):
            try :
                answer=int(input(f"{x} + {y} ="))
                if answer==(x+y):
                    score+=1
                    break
                elif i==3:
                    print(f"{x} + {y} = {x+y}")
                else:
                    print("EEE")
            except ValueError:
                pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if(level>=1 and level<=3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level ==1:
        a=0
        b=9
    elif level==2:
        a=10
        b=99
    elif level==3:
        a=100
        b=999
    return random.randint(a,b)


if __name__ == "__main__":
    main()