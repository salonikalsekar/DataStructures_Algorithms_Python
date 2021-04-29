def quick_sort(arr):

    i=0
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller = []
        larger = []
        equal = []
        while i < len(arr):
            if arr[i] < pivot:
                smaller.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                larger.append(arr[i])
            i+=1
        print(smaller, equal, larger)

    return quick_sort(smaller) + equal + quick_sort(larger)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quick_sort(l))

# [1, 4, 3, 2] [5] [6, 8, 10, 7, 8, 9]
# [1] [2] [4, 3]
# [] [3] [4]
# [6, 8, 7, 8] [9] [10]
# [6, 7] [8, 8] []
# [6] [7] []
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
