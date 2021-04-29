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


def merge_sorted(arr1, arr2):
    sorted = []
    i,j =0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted.append(arr1[i])
            i += 1
        else:
            sorted.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted.append(arr2[j])
        j += 1
    return sorted

def MergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2

        l1 = MergeSort(arr[middle:])
        l2 = MergeSort((arr[:middle]))

    return merge_sorted(l1, l2)


def bubble_sort(l):
    swap = True
    while swap:
        # print(l)
        swap=False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                swap=True
                l[i], l[i+1] = l[i+1], l[i]
