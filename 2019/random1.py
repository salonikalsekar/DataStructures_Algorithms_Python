def topNCompetitors():

    num1 = 6
    top = 2
    comp = ["beta", "delta", "cetra", "eurocell", "anacell", "cetra"]

    numreviews = 6

    reviews = ["beta delta is the best", "cetra eurocell", "anacell anacell", "beta", "beta cetra"]
    final = []
    d = {}
    d1 = {}
    reviews_unique = set(reviews)
    for i in reviews_unique:
        s = i.split()

        for word in s:
            if word in comp:
                if word in d:
                    d[word] +=1
                else:
                    d[word] = 1
    d1= {}

    for k,v in d.items():
        if v in d1:
            d1[v].append(k)
        else:
            d1[v] = [k]


    sorted_dict = sorted(d1.items(),reverse=True)
    sorted_dict[0][1].append("saloni")
    for i in sorted_dict:
            final += sorted(i[1])

    if len(final) < top:
        return final

    else:
        return final[:top]

print(topNCompetitors())



