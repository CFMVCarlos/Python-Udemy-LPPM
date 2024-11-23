import csv

csv_filename = "Section8/cereal_grains.csv"
with open(csv_filename, encoding="utf-8", newline="") as csv_file:
    #! csv.QUOTE_NONNUMERIC can only be used when the strings in the CSV file are quoted.
    #! This converts all non-quoted fields to floats.
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
