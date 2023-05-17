import random
import sys
while True:
    try:
        level=int(input("Level: "))
        if(level>1):
            break
    except ValueError:
        pass
generated= random.choice(range(1,level))
while True:
    try :
        guess=int(input("Guess: "))
        if guess<1:
            continue
        elif guess==generated:
            sys.exit("Just right!")
        elif guess < generated:
            print("Too small!")
        elif guess > generated:
            print("Too large!")
    except ValueErrork:
        pass



