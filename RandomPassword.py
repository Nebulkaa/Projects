import random

def generatePassword():
    password = ""
    length = random.randint(12, 18)
    for i in range(length):
        char = random.randint(32, 126)
        char = chr(char)
        password = password + char
    print(password)
    
generatePassword()