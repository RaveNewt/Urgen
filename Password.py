import random, string

def Password_random():
    password_length = int(input("How long do you want the password to be:"))

    password_character = string.ascii_letters + string.digits + string.punctuation
    password = []

    for x in range(password_length):
        password.append(random.choice(password_character))

    print(''.join(password))
print(Password_random())