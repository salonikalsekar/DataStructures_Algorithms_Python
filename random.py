def random(N, K):
    res = []
    val = ""
    printAll(3, val, res)
    print(res)


def printAll(N, val, res):
    alph = ["a", "b", "c"]
    if N == 0:
        res.append(val)
        return

    for i in range(len(alph)):
        newVal = val + alph[i]
        printAll(N-1, newVal, res)





















set1 = ['a', 'b']
k = 3
random(set1, k)