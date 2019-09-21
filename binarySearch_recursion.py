def binarySearch_recur(n, arr, start, end):
    if start > end:
        return "not found"

    mid = (start + end) // 2
    if arr[mid] == n:
        return f"{n} found at position {mid}"
    elif arr[mid] < n:
        return binarySearch_recur(n, arr, mid + 1, end)
    else:
        return binarySearch_recur(n, arr, start, mid - 1)




l = [1,2,3,4,5,6,7,8,9,10]

searchNum = 5
print(binarySearch_recur(searchNum, l, 0, len(l) - 1))


# we do not create slice array bcz it creates a new copy everytime and we need the idex in the original list of the value to be searched