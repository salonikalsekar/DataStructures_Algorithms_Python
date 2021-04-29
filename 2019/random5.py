from collections import Counter
def test(literatureText, wordsToExclude):
    s = literatureText.lower()

    puncList = ['!', '?', "'", ',', ';', '.']
    for i in puncList:
        s = s.replace(i, " ")

    s1 = s.split()
    d = Counter(s1)


    for i in wordsToExclude:
        i = i.lower()
        del d[i]
    maxValue = max(d.values())

    keyList = [k for k, v in d.items() if v == maxValue]
    return keyList

print(test("is is a a d d f f dddd dddsdsd dsdsd ddf", ["dddd", "dddsdsd", "dsdsd", "ddf"]))