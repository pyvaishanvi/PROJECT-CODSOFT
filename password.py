import random
import string

print("== Password Generator ==")

length = int(input("Enter the length of password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length) )

print(f"Generated Password: {password}")
