from prac_06 import guitar
from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = input("Cost: ")
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # if guitars:
    #     print("These are my guitars")
    #     for i, guitar in enumerate(guitars, 1):
    #         vintage_string = " "
    #         if guitar.is_vintage():
    #             vintage_string = "Vintage"
    #         # else:
    #         #     vintage_string = "not vintage"
    #         print(f"Guitar {i}: {guitar.name:>10} ({guitar.year}), worth ${guitar.cost:>7} is {vintage_string}")
    # else:
    #     print("You have no guitars")

# ------   is_vintage() not working in this program ----------

    if guitars:
        print("These are my guitars")
        for guitar in guitars:
            vintage_string = " "
            if guitar.is_vintage():
                vintage_string = "Vintage"
                print(f"Guitar {guitar}: {guitar.name:>10} ({guitar.year}), worth ${guitar.cost:>7} is {vintage_string}")
    else:
        print("You have no guitars")

main()
