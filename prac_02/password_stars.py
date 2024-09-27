MIN_LENGTH = 8
password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print("invalid password")
    password = input("Enter a password: ")
print(f"Your password is:", "*" * len(password))