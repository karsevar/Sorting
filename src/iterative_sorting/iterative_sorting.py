# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j 

        # TO-DO: swap
        # arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        current_value = arr[cur_index] 
        smallest_value = arr[smallest_index]
        arr[cur_index] = smallest_value 
        arr[smallest_index] = current_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = True
    swap_counter = 0

    while swap_occured:
        for cur_index in range(0, len(arr) - 1):
            if arr[cur_index] > arr[cur_index + 1]:
                arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index] 
                swap_counter += 1

        if swap_counter == 0:
            swap_occured = False
        else:
            swap_occured = True
            swap_counter = 0

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr