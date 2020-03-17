# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr.append(arrB.pop(0))
        elif len(arrB) == 0:
            merged_arr.append(arrA.pop(0))
        elif arrA[0] >= arrB[0]:
            merged_arr.append(arrB.pop(0))
        elif arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
       
    
    return merged_arr

# print(merge([],[2,3]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Split the input arr in half and place the left and right sides 
    # into the merge helper function 
    if len(arr) > 1:
        mid = (len(arr)) // 2
        print(arr[:mid])
        print(arr[mid:])
        LHS = merge_sort(arr[:mid])
        RHS = merge_sort(arr[mid:])
        arr = merge(LHS, RHS)


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
        print('arr', arr)
        pivot = arr[0]
        print('pivot', pivot)
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

print(quick_sort([3,1,6,3,2,3]))




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
