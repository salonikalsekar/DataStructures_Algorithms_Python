def urlify(s1):
    c = 0
    for i in s1:
        if i == ' ':
            c += 1

    l = len(s1) - 1
    newLength = (l) + (c * 2)

    s = ['' for x in range(newLength + 1)]

    while l >= 0:
        if s1[l] == " ":
            s[newLength] = "0"
            s[newLength - 1] = "2"
            s[newLength - 2] = "%"
            newLength -= 3
        else:
            s[newLength] = s1[l]
            newLength -= 1

        l -= 1

    return ''.join(s)




print(urlify("the i fbkfjf "))