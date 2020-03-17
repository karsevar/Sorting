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

def insertion_sort(arr):
    # start with the first value in the array 

    # start a loop discounting of course the first index position

    #   save the current index element in a variable 
    #   start a loop that will start at the last index position 
    #       check if the current index is less than the inner current index
    #           insert the value in the inner current index 
    #       else don't do anything

    for i_index in range(1, len(arr)):
        cur_index = i_index 

        for j_index in range(0, cur_index):
            # print(f'Is {arr[cur_index]} less than {arr[j_index]}: {arr[j_index] > arr[cur_index]}')
            if arr[j_index] > arr[cur_index]:
                arr.insert(j_index, arr.pop(cur_index))
    return arr

print(insertion_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # create a count array at is the total size of the largest number plus one to 
    # make room for the zero

    # loop through the array counting each occurance of each value in the count array.

    # loop through the count array and place the index positions in a new array with the 
    # proper amount of reoccurence.
    if len(arr) == 0:
        return []

    maximum = max(arr)
    
    count_array = [0] * (maximum + 1)
    new_array = []
    
    for count in arr:
        if count < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count_array[count] += 1

    for index_count in range(len(count_array)):
        for _ in range(count_array[index_count]):
            new_array.append(index_count)

    return new_array

print(count_sort([2,3,1,7]))