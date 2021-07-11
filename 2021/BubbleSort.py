

def bubbleSort(arr):
    swapped = True
    while swapped:
        for n in range(len(arr) - 1):
            swapped = False
            if arr[n] > arr[n+1]:
                swapped = True
                arr[n], arr[n+1] = arr[n+1], arr[n]

    return arr


print(bubbleSort([2,1,3,4,5]))