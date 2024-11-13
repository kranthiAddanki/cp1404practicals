from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitar.csv", 'r')
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
        print(guitar)
    in_file.close()


main()
