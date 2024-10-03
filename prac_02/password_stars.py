
MIN_LENGTH = 8


def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    print(f"Your password is:", "*" * len(password))


def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print("invalid password")
        password = input("Enter a password: ")
    return password


main()
