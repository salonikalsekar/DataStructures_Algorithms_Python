def binarySearch_recur(n, arr, start, end):
    if start > end:
        return f"{n} not found"

    else:
        middle = (start + end) // 2
        if n == arr[middle]:
            return f"{n} found at {middle}"
        elif n > arr[middle]:
            return binarySearch_recur(searchNum, arr, middle + 1, end)
        else:
            return binarySearch_recur(searchNum, arr, start, middle - 1)


# to test various array size
def createList(maxValue):
    arr = []
    for num in range(1, maxValue):
        arr.append(num)

    return arr

l = createList(10)

searchNum = 9
print(binarySearch_recur(searchNum, l, 0, len(l) - 1))


# we do not create slice array bcz it creates a new copy everytime and we need the idex in the original list of the value to be searched