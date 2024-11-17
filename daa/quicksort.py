import random
import time

def quick_sort(arr, low, high):

    if low < high:
        pivot_index = Randomizer(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)



def Randomizer(arr, low, high):
    pivotindex = random.randint(low, high)
    arr[pivotindex], arr[high] = arr[high], arr[pivotindex]
    return Partition(arr, low, high)

def Partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [0, 10, 87, 9]
quick_sort(arr, 0, 3)
print(arr)
