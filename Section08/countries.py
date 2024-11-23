input_filename = "Section8/country_info.txt"

countries: dict[str, dict[str, str]] = {}
with open(input_filename) as country_file:
    # Read the header
    header: str = country_file.readline()
    # Read the data
    for row in country_file:
        data: list[str] = row.strip("\n").split("|")
        # print(data)
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict: dict[str, str] = {
            "country": country,
            "capital": capital,
            "code": code,
            "code3": code3,
            "dialing": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        #! This will reference the same dictionary in memory
        #! It will increase the size of the dictionary but not by much
        #! It allows to search by name and code
        countries[code.casefold()] = country_dict
    # print(countries)

while True:
    print()
    user_country_name: str = input("Enter a country name or code: ").casefold()
    if user_country_name in countries:
        print(
            f"-> The capital of {user_country_name.capitalize()} is {countries[user_country_name]['capital']}"
        )
    elif user_country_name == "exit":
        print("Goodbye!")
        break
    else:
        print("Country not found")
