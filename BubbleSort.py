import  array as ar
from array import array

arr = ar.array("i",[15, 10, 64, 34, 25, 12, 22, 11, 90,20])

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                #arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


sorted_ar = bubble_sort(arr)
print(f"Array is sorted now: {sorted_ar}")