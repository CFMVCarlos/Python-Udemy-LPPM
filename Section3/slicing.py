string = "Norwegian Blue"

print(string[3], string[4], string[9], string[3], string[6], string[8])


print(string[-11], string[-10], string[-5], string[-11], string[-8], string[-6])

print(
    string[3 - 14],
    string[4 - 14],
    string[9 - 14],
    string[3 - 14],
    string[6 - 14],
    string[8 - 14],
)

print("------------")

print(string[3:7], string[:9], string[10:], sep=", ")
print(string[-7:-3], string[:-5], string[-4:], sep=", ")
print(string[0:6:2], string[:9:2], string[10::2], string[::2], sep=", ")
print(string[::-1])

print("------------")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[16:13:-1], alphabet[4::-1], alphabet[:-9:-1], sep=", ")

print("------------")

print(f"Pi is approximately {22/7:<72.50f}")
