def main():
    email_to_name = {}
    email = input('Enter your email: ')
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your {name} correct? (Y/N)")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Enter your name:")
        email_to_name[email] = name
        email = input('Enter your email: ')

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
