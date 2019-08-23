def insertSort(l):
    i = 1
    j= i-1
    while i <len(l):
        print(l)
        while j >= 0 and l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                i -= 1
                j -= 1

        i += 1
        j += 1


l = [6,8,1,4,10]

insertSort(l)



# Iterations
# [6, 8, 1, 4, 10]
# [6, 8, 1, 4, 10]
# [1, 6, 8, 4, 10]
# [1, 6, 8, 4, 10]
# [1, 6, 8, 4, 10]
# [1, 4, 6, 8, 10]
# [1, 4, 6, 8, 10]
# [1, 4, 6, 8, 10]