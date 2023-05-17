from validator_collection import validators,errors

def main():
    try:
        email=validators.email(input("Email: "))
    except errors.InvalidEmailError:
        print("Invalid")
    else:
        print("Valid")

if __name__=="__main__":
    main()