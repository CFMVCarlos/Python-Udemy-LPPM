import os

root = "Section12\\music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split: tuple[str, str] = os.path.split(path)
        print(first_split)
        second_split: tuple[str, str] = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f.removesuffix(".emp3").split(" - ")
            print(song_details)
        print("*" * 80)
    # print(directories)
    # print(files)
    # input()
    # for f in files:
    #     print(f"\t{f}")
