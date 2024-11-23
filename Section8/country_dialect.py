import csv

input_filename = "Section8/country_info.txt"
with open(input_filename, encoding="utf-8", newline="") as countries_data:
    #! Automatic dialect detection

    #! One way is to read the entire file
    # sample = countries_data.read()
    #! Another way is to read the first few lines
    sample: str = "".join([countries_data.readline() for _ in range(5)])
    #! Uses the sniffer to determine the dialect
    country_dialect = csv.Sniffer().sniff(sample)
    #! Removes the initial space of the strings
    country_dialect.skipinitialspace = True
    #! Resets the file pointer to the beginning of the file
    countries_data.seek(0)
    #! Creates a reader object using the determined dialect
    country_reader = csv.reader(countries_data, dialect=country_dialect)

    #! Manual delimiter definition
    # country_reader = csv.reader(countries_data, delimiter="|")
    for row in country_reader:
        print(row)

#############################################################################################################################
print(f"\n{"*"*80}\n")
#############################################################################################################################
attributes = ['delimiter', 'doublequote', 'escapechar', 'lineterminator', 'quotechar', 'quoting', 'skipinitialspace']

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
