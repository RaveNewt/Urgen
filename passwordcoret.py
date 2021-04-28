import urllib.request
import random, string
def Password():
    password_length = int(input("How long do you want the password to be:"))
    password_length1 = password_length/2
    word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    x = random.randrange(0,len(words)+1)
    eWord = words[x]

    password_character = string.ascii_letters + string.digits + string.punctuation 
    password = []
    while (len(eWord) > password_length):
        eWord = words[x]

    password.append(eWord)
    for z in range(password_length - len(eWord)):
        password.append(random.choice(password_character))
    print(''.join(password))
print(Password())