import random
import string
import datetime

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="password_db.txt"):
    with open(filename,"a") as file:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{date}, {password}\n")
print("Password has been saved in 'password_db.txt'")
                    