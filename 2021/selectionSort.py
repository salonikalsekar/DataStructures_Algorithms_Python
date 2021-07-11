def selectionSort(arr):
    marker = 0
    while marker < len(arr):
        for n in range(marker, len(arr)):
            if arr[marker] > arr[n]:
                arr[marker], arr[n] = arr[n], arr[marker]
        marker += 1

    return arr


print(selectionSort([2,1,3,4,5]))