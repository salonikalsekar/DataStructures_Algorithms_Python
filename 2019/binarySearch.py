def binarySearch(n, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return f"{n} found at {mid}"
        elif arr[mid] < n:
            start = mid + 1
        else:
            end= mid - 1
    return f"{n} not found"


l = [1,2,3,4,5,6,7,8,9,10]

searchNum = 11
print(binarySearch(searchNum, l))



# we do not create slice array bcz it creates a new copy everytime and we need the index in the original list of the value to be searched