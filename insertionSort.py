def insertionSort(arr):

    print(arr)
    key = 1
    while key < len(arr):
        for i in range(key,0,-1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        key += 1
        print(arr)
    return arr


l = [6,1,8, 4,10]

print(insertionSort(l))

# Iterations
#
# [6, 8, 1, 4, 10]
# [6, 1, 8, 4, 10]
# [6, 1, 4, 8, 10]
# [6, 1, 4, 8, 10]