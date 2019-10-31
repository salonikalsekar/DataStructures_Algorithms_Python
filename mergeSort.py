def divideArray(arr):
    if len(arr) <= 1:
        return arr[:]
    arrLength = len(arr) // 2
    print("firstPart", arr)
    leftArray = divideArray(arr[:arrLength])
    rightArray = divideArray(arr[arrLength:])
    print("secondPart")
    print(leftArray, rightArray)
    return mergeArrays(leftArray, rightArray)

def mergeArrays(arr1, arr2):
    print("merge", arr1, arr2)
    sorted=[]
    i,j = 0,0
    while i< len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            sorted.append(arr1[i])
            i+= 1
        else:
            sorted.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted.append(arr2[j])
        j += 1
    print("sorted", sorted)
    return sorted

########## Main Execution - Divide and Conquer - Merge Sort ###########
l = [6,8,1,4,10,7,8,9,3,2,5]
print(divideArray(l))

# firstPart [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# firstPart [6, 8, 1, 4, 10]
# firstPart [6, 8]
# secondPart
# [6] [8]
# merge [6] [8]
# sorted [6, 8]
# firstPart [1, 4, 10]
# firstPart [4, 10]
# secondPart
# [4] [10]
# merge [4] [10]
# sorted [4, 10]
# secondPart
# [1] [4, 10]
# merge [1] [4, 10]
# sorted [1, 4, 10]
# secondPart
# [6, 8] [1, 4, 10]
# merge [6, 8] [1, 4, 10]
# sorted [1, 4, 6, 8, 10]
# firstPart [7, 8, 9, 3, 2, 5]
# firstPart [7, 8, 9]
# firstPart [8, 9]
# secondPart
# [8] [9]
# merge [8] [9]
# sorted [8, 9]
# secondPart
# [7] [8, 9]
# merge [7] [8, 9]
# sorted [7, 8, 9]
# firstPart [3, 2, 5]
# firstPart [2, 5]
# secondPart
# [2] [5]
# merge [2] [5]
# sorted [2, 5]
# secondPart
# [3] [2, 5]
# merge [3] [2, 5]
# sorted [2, 3, 5]
# secondPart
# [7, 8, 9] [2, 3, 5]
# merge [7, 8, 9] [2, 3, 5]
# sorted [2, 3, 5, 7, 8, 9]
# secondPart
# [1, 4, 6, 8, 10] [2, 3, 5, 7, 8, 9]
# merge [1, 4, 6, 8, 10] [2, 3, 5, 7, 8, 9]
# sorted [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]