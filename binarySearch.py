def binarySearch(n, arr):
    start = 0
    end = len(arr) - 1

    while start<=end:
        middle = (start + end) // 2
        if n == arr[middle]:
            return f"{n} found at {middle}"
        elif n > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return f"{n} Not found"


# to test various array size
def createList(maxValue):
    arr = []
    for num in range(1, maxValue):
        arr.append(num)

    return arr

l = [1,2,3,4,5,6,7,8,9,10]

searchNum = -1
print(binarySearch(searchNum, l))