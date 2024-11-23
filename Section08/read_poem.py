# Description: Reading a file in Python
#! Default mode is read mode
# jabber = open("Jabberwocky.txt", "r")
# for line in jabber:
#! First way involves using the end parameter of the print function
# print(f"{len(line):2} | {line}", end="")
#! Second way involves using the right strip method (rstrip) to remove the newline character
# print(f"{len(line):2} | {line.rstrip()}")
# jabber.close()

#############################################################################################################################
# print(f"\n{"*"*80}\n")
#############################################################################################################################

#! This is the correct way to open a file in Python
with open("Section8/Jabberwocky.txt", "r", encoding='utf-8') as jabber:
    for line in jabber:
        print(f"{len(line):2} | {line.rstrip()}")

#############################################################################################################################
print(f"\n{"*"*80}\n")
#############################################################################################################################

#! This should only be used for small files as it reads the entire file into memory
#! Returns the entire file as a list of strings
# with open("Jabberwocky.txt") as jabber:
#     lines: list[str] = jabber.readlines()
# print(lines)

#############################################################################################################################
# print(f"\n{"*"*80}\n")
#############################################################################################################################

#! Returns the entire file as a single string
# with open("Jabberwocky.txt") as jabber:
#     text: str = jabber.read()
# print(text)

#############################################################################################################################
# print(f"\n{"*"*80}\n")
#############################################################################################################################

#! Readline is used to read a single line from a file
#! Not used often as it is not efficient as can be substituted with a for loop
# with open("Jabberwocky.txt") as jabber:
#     while True:
#         line: str = jabber.readline().rstrip()
#         print(line)
#         if "jubjub" in line.casefold():
#             break
