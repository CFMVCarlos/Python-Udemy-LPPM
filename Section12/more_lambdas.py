anon = lambda x: x * 2  # Not PEP8 compliant, but it's a common convention


def double(x):
    return x * 2


print(anon)
print(double)

print(anon(10))
print(double(10))
