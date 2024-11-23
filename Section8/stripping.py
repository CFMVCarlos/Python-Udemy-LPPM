filename = "Section8/Jabberwocky.txt"
with open(filename) as poem:
    first: str = poem.readline().rstrip()

print(first)


#! This removes the characters from the beginning and end of the string
#! Even if all the characters are not present in the string
#! It checks for the presence of the characters in the string one by one
chars = "'Twasebv"
no_apostrophes = first.strip(chars)
print(no_apostrophes)

#############################################################################################################################
print("*" * 80)
#############################################################################################################################

#! To remove a string from the beginning or end of a string use removeprefix or removesuffix
twas_removed = first.removeprefix("'Twas ")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)
