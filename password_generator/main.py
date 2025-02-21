import utils

def main():
    
    try:
        length = int(input("Type in the length of the password: "))
    except ValueError:
        print("Please eneter a valid length")
        return

    
    password = utils.generate_password(length)
    print("Password has been generated", password)
    
    
    utils.save_password(password)

if __name__ == "__main__":
    main()
