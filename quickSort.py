def quickSort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for i in arr:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                larger.append(i)

        return quickSort(smaller) + equal + quickSort(larger)



l = [6,8,1,4,10,7,8,9,3,2,5]
print(quickSort(l))