def quickSort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[-1]
    smaller, larger, equal = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quickSort(smaller) + equal + quickSort(larger)


print(quickSort([2,3,12,4,5,7]))