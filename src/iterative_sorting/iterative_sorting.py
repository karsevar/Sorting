# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
            print('smallest in inner loop', arr[smallest_index])

        print('smallest after first loop', arr[smallest_index])
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        
             



        # TO-DO: swap




    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # create the loop structure that will repeat if a swap boolean reads true 

    # if the right side of the current index is smaller swap the two values.
    #   set boolean to true
    # if the current index is smaller than the right side don't do anything.
    swap_bool = True
    swap_counter = 0

    while swap_bool:
        for cur_index in range(len(arr)-1):
            if arr[cur_index] > arr[cur_index +1]:
                arr[cur_index], arr[cur_index+1] = arr[cur_index+1], arr[cur_index]
                swap_counter += 1 

        if swap_counter == 0:
            swap_bool = False
        else: 
            swap_counter = 0
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr