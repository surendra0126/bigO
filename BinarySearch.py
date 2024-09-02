import array as arr
from array import array
from tarfile import tar_filter

arr1 = arr.array('i',[10,15,77,50,60,100,102,105,200,208,500,505])

def binary_search_for_loop(my_arr,tar: int) ->  int:
    low: int = 0
    high: int = len(my_arr)-1

    for i in range(len(my_arr)):
        if low > high :
            return -1
        middle: int = int((int(low) + int(high)) / 2)
        if my_arr[middle] == tar:
            return middle
        elif my_arr[middle] < tar:
            low = middle + 1
        else:
            high = middle -1
    return -1

def binary_search_while_loop(my_arr,tar: int) ->  int:
    low: int = 0
    high: int = len(my_arr)-1

    while low<=high :
        middle: int = int((int(low) + int(high)) / 2)

        if my_arr[middle] == tar:
            return middle
        elif my_arr[middle] < tar:
            low = middle + 1
        else:
            high = middle -1
    return -1

target : int = 1000
index:int = binary_search_while_loop(arr1,target)

print(f'target value {target} found in index {index}')




