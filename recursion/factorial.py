
def factiter(n):
    prod = 1
    while n > 1:
        prod *= n
        n = n-1

    print(prod)

factiter(5)


def factrecur(n):
    if n>0:
        return n * factrecur(n-1)
    else:
        return 1

print(factrecur(3))
