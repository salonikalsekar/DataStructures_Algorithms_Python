def isUnique(s):
    res = []
    for i in range(129):
        res.append(False)

    for i in range(len(s)):
        v = ord(s[i])
        if res[v]:
            return False

        res[v] = True

    return True


def isUniqueV2(s):
    s = sorted(s)
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return False

    return True








print(isUnique("salonii"))
print(isUniqueV2("saloni"))