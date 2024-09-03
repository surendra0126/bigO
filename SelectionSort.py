import numpy as np

#use numpy to get array
arr = np.array([4,3,2,6,8,0,1])

def selection_sort(ar):
    size = len(ar)
    for i in range(size):
        mid = i
        for j in range(i+1,size):
            if ar[mid] > ar[j] :
                mid = j
        #ar[i],arr[mid] = ar[mid],ar[i]
        temp = ar[i]
        ar[i] = ar[mid]
        ar[mid] = temp

    print(ar)

selection_sort(arr)

