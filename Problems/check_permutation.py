from collections import defaultdict
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    r = defaultdict(int)

    for i in s1:
        r[i] += 1

    print(r)
    for j in s2:
        r[j] -= 1
        print(r)
        if r[j] < 0:
            return False

    return True

print(checkPermutation("ssl", "sal"))


