def main():
    records =[]
    with open("wimbledon.csv", "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
#        print(records)

    champions_to_count, countries = process_records(records)
    print(champions_to_count)
    print(countries)
    display(champions_to_count, countries)

def process_records(records):

    champions_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champions_to_count[record[2]] += 1
        except KeyError:
            champions_to_count[record[2]] = 1
    return champions_to_count, countries

def display(champions_to_count, countries):
    print("Champions in the Wimbledon are:")
    for name, count in champions_to_count.items():
        print(name, count)
    print(f"The athelets from these {len(countries)} countries won the wimbledon championship:")
    print(", ".join(country for country in sorted(countries)))




main()