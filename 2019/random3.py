def s1(s , n):
    s2 = []
    for i in range(len(list(s))):
        if len(set(s[i:i+n])) == n:
            s2.append(s[i:i+n])

    print(set(s2))


s1("abcd", 3)