import csv

input_filename = "Section8/country_info.txt"

dialect = csv.excel
dialect.delimiter = "|"

countries: dict[str, dict[str, str]] = {}
with open(input_filename) as country_file:
    # Get the column heading from the first line of the file
    headings: list[str] = next(csv.reader(country_file, delimiter=dialect.delimiter))
    headings = [heading.casefold() for heading in headings]

    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row["country"].casefold()] = row
        countries[row["cc"].casefold()] = row

print(countries)

while True:
    print()
    user_country_name: str = input("Enter a country name or code: ").casefold()
    if user_country_name in countries:
        print(
            f"-> The capital of {countries[user_country_name]['country']} is {countries[user_country_name]['capital']} with code {countries[user_country_name]['cc']}"
        )
    elif user_country_name in ("exit", "quit"):
        print("Goodbye!")
        break
    else:
        print("Country not found")
