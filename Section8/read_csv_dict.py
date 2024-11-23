import csv

cereals_fileame = "Section8/cereal_grains.csv"
with open(cereals_fileame, encoding="utf-8", newline="") as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
