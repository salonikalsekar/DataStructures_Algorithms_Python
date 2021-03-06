

def selectionSort(arr):
    marker = 0
    while marker < len(arr):
        for j in range(marker, len(arr)):
            if arr[marker] > arr[j]:
                arr[marker], arr[j]= arr[j], arr[marker]
        marker += 1
        print(arr)


l = [6,8,1,4,10,7,8,9,3,2,5]

selectionSort(l)



# Iterations
# [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# [1, 8, 6, 4, 10, 7, 8, 9, 3, 2, 5]
# [1, 2, 8, 6, 10, 7, 8, 9, 4, 3, 5]
# [1, 2, 3, 8, 10, 7, 8, 9, 6, 4, 5]
# [1, 2, 3, 4, 10, 8, 8, 9, 7, 6, 5]
# [1, 2, 3, 4, 5, 10, 8, 9, 8, 7, 6]
# [1, 2, 3, 4, 5, 6, 10, 9, 8, 8, 7]
# [1, 2, 3, 4, 5, 6, 7, 10, 9, 8, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]


# Time Complexity O(n**2)