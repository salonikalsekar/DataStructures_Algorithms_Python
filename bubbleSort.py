

def bubbleSort(arr):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(arr) - 1):
            print(i)
            if arr[i] > arr [i+1]:
                arr[i], arr[i+1]= arr[i+1] , arr[i]
                swap = True
        print(arr)





l = [6,8,1,4,10,7,8,9,3,2,5]

bubbleSort(l)

# # Iterations
# # [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# # [6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
# # [1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10]
# # [1, 4, 6, 7, 8, 3, 2, 5, 8, 9, 10]
# # [1, 4, 6, 7, 3, 2, 5, 8, 8, 9, 10]
# # [1, 4, 6, 3, 2, 5, 7, 8, 8, 9, 10]
# # [1, 4, 3, 2, 5, 6, 7, 8, 8, 9, 10]
# # [1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 10]
# # [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

 # Time Complexity O(n**2)