# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    print('arrA', arrA, 'arrB', arrB)

    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr.append(arrB.pop(0))
        elif len(arrB) == 0:
            merged_arr.append(arrA.pop(0))
        elif arrA[0] >= arrB[0]:
            merged_arr.append(arrB.pop(0))
        elif arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
       
    # print(merged_arr)
    return merged_arr

# print(merge([],[2,3]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Split the input arr in half and place the left and right sides 
    # into the merge helper function 
    if len(arr) > 1:
        mid = (len(arr)) // 2
        # print(arr[:mid])
        # print(arr[mid:])
        LHS = merge_sort(arr[:mid])
        RHS = merge_sort(arr[mid:])
        arr = merge(LHS, RHS)

        print('array in main function', arr)

    return arr

# print(merge_sort([2,3,1,6,1,2]))

# quick sort:
def quick_sort(arr):
    # find the pivot of the array (usually the first element) 

    # if array length is 1 return the element as an array (base case)

    # split the array according to the elements being greater than or less than
    # the pivot 

    # recursively call the function between the left side and right side

    if len(arr) > 1:
        # print('arr', arr)
        pivot = arr[0]
        # print('pivot', pivot)
        LHS = []
        RHS = []

        # stupidly forgot to not include the pivot in the LHS and RHS calculations 
        # if you include the pivot value the algorithm will create an infinite loop.
        for element in arr[1:]:
            if pivot > element:
                LHS.append(element) 
            else:
                RHS.append(element) 

        LHS = quick_sort(LHS) 
        RHS = quick_sort(RHS)

        arr = LHS + [pivot] + RHS

    return arr

# print(quick_sort([3,1,6,3,2,3]))




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    # separate the left and right arrays my the mid point.
    # example: arrA = arr[start:mid], arrB = arr[mid:end]

    # index variables to partition arrA and arrB elements.
    # create an i index start at start index
    # create a j index start at mid index

    # for loop which iterates a total of len(arr[start:end]), start index is start 
    # and end index is end
        # if arr[i] > arr[j]:
            # arr[i], arr[j] = arr[j], arr[i]
            # j += 1
        # if arr[i] < arr[j]:
            # arr[j], arr[i] = arr[i], arr[j]

    i = 0 
    j = 0
    L = arr[start:mid]
    R = arr[mid:end]
    k = start

    for index in range(k, end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            arr[index] = L[i]
            i += 1
        else:
            arr[index] = R[j]
            j += 1
        

        # print('arrA', arr[start:mid+1], 'arrB', arr[mid+1:end+1])
        # print('inplace array', arr)

    return arr

# print(merge_in_place([4,1,1,3,2], 0, 2, 4))

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    # base case if length of array is less than 1 return nothing.

    # create the mid point variable. save the index as a variable.
    # mid = (end + start) // 2

    # Separate the array by leftside and rightside according to the mid point variable

    # recursive call the merge_sort function for both the leftside and rightside 
    # partitions make sure to pass left and right indexes in the function 

    # merge the left and right sides together through the merge_in_place function.
    # make sure to pass in the start, end, and mid indexes.

    if len(arr[l:r]) > 1:
        mid = (l + r) // 2
        # print('LHS array in main merge function', arr[l:mid])
        # print('RHS array in main merge function', arr[mid:r])
        # print('indexes in the recursion low:', l, 'right', r)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)

        

        arr = merge_in_place(arr, l, mid, r)

    return arr

print(merge_sort_in_place([2,1,6,3,4,2], 0, 6))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
