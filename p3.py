import random
import string

length = int(input("Enter the password length: "))

if length < 2:
    print("Password length must be at least 2.")
else:
    letters = string.ascii_letters
    numbers = string.digits

    password = [
        random.choice(letters),
        random.choice(numbers)
    ]

    
    characters = letters + numbers

    for _ in range(length - 2):
        password.append(random.choice(characters))

    
    random.shuffle(password)

    password = ''.join(password)

    print("Generated Password:", password)
