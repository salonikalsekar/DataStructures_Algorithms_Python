def reverseString(s):
    if not s:
        return ""

    s1 = s[-1]
    s1 +=  reverseString(s[:-1])

    return s1



print(reverseString("abcde"))




