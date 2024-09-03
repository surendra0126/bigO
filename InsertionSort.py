import array as arr

#declare an array
arr_list = arr.array("b",[4,3,2,1,5,8,22])

#funciton definition
def insertion_sort(list):
    for i in range(1,len(list)):
        #set the value from index 1 to key = 3
        key = arr_list[i]
        j = i - 1
        while j >=0 and key < list[j]:
            #if key which is value of right side is less, then replace with prev one
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = key

    print(list)

insertion_sort(arr_list)
