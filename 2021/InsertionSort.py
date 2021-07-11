def insertionSort(arr):
    pointer = 1
    while pointer < len(arr):
        working_index = pointer
        f = True
        while working_index > 0 and f:
            if arr[working_index] < arr[working_index - 1]:
                f = True
                arr[working_index -1], arr[working_index] = arr[working_index], arr[working_index-1]
                working_index -= 1
            else:
                f = False

        pointer += 1
    return arr

print(insertionSort([6,1,8,4,10, 14, 22,2,2,5,4,3,4,2,45]))