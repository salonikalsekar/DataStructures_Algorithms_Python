
import random
from demo import quickSort
from demo import MergeSort
from demo import bubble_sort

import time


def createRandom(size, maxValue):
    list1 = []
    for num in range(size):
        list1.append(random.randint(1,maxValue))

    return list1

def analyse(funcName, l):
    tic = time.time()
    funcName(l)
    toc = time.time()
    elapsedTime =  toc - tic
    print(f"{funcName.__name__.capitalize()}\t -> Elapsed Time --> {elapsedTime:.5f}")

size = int(input("Enter the size of the list: "))
maxValue = int(input("Enter the maximum value range: "))
l = createRandom(size, maxValue)

runTime = int(input("Number of times you want the program to run? "))


for num in range(runTime):
    print(f"Run: {num + 1}")
    analyse(bubble_sort, l.copy())
    analyse(quickSort, l)
    analyse(MergeSort, l)
    analyse(sorted, l)
    print("-" * 60)
