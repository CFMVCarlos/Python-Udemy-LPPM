import csv

csv_filename = "Section8/OlympicMedals_2020.csv"
#! The newline argument is used to prevent the csv module from adding an extra newline character to the end of each row.
with open(csv_filename, encoding="utf-8", newline="") as csv_file:
    reader = csv.reader(csv_file)
    headers: list[str] = next(reader)
    print(f"Column headers: {headers}")
    for row in reader:
        print(row)
