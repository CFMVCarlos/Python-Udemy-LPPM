# equation: bytes = bytes((207, 128, 114, 194, 178))
equation: bytes = b"\xcf\x80r\xc2\xb2"
# [0xCF, 0x80, 0x72, 0xC2, 0xB2]
# \xcf\x80 = π, \xc2\xb2 = ²

print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=", ")
print()

for b in equation:
    print(hex(b), end=", ")
print()

print(equation.decode("utf-8"))
