import csv

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Imelda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

keys = ["album", "artist", "year"]


filename = "Section8/albums.csv"
with open(filename, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip_object:
        #     print("\t", thing)
        albums_dict = dict(zip_object)
        writer.writerow(albums_dict)
        # print(albums_dict)