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

print(merge_sort([2,3,1,6,1,2]))


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
