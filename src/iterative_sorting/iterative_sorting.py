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

    if len(arr) == 0:
        return []

    # find the maximum value in the array
    maximum_value = max(arr) 

    # create a count array. plus one to count for the occurance of zero.
    count_array = [0] * (maximum_value + 1)

    # create a loop that will iterate through the array counting the occurance of integers and puttin them in 
    # their corresponding indexes.
    for index in arr:
        if index < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count_array[index] += 1

    # Go through the count_array again and calculate the counts in ascending order:
    for count_index in range(0, len(count_array)):
        if count_index == 0:
            count_array[count_index] = count_array[count_index]
        else:
            count_array[count_index] += count_array[count_index - 1]

    # Go through the count_array and translate the values to the left as a means to calculate the starting indexes:
    count_array = [0] + count_array[: -1]

    # create a new array for results.

    # write a loop that will go through each value in arr.
        # place value in start index position of new array 
        # increment the start position in the count_array

    new_array = [0] * len(arr) 

    for value in arr:
        new_array[count_array[value]] = value 
        count_array[value] += 1 

    return new_array

print(count_sort([1,5,3,6]))