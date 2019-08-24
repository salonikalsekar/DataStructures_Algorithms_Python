#Merge the sorted divided lists
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

# l1 = [1,4,6,8,10]
# l2 = [2,3,5,7,8,9,13,44]
# merge_sorted(l1, l2);

# Iterations for merge_sorted function:
# []
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 8]
# merged list: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

#Divide
def divideArr(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2

        l1 = divideArr(arr[middle:])
        l2 = divideArr((arr[:middle]))

        return merge_sorted(l1, l2)



########## Main Execution - Divide and Conquer - Merge Sort ###########
l = [6,8,1,4,10,7,8,9,3,2,5]
print(divideArr(l))
