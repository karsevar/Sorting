# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
    
#     return merged_arr

def merge(a, b):
	elements = len(a) + len(b)
	merged_arr = [0] * elements

	# starting at beginning of a and b

	i = 0 
	j = 0 
	k = 0
	
	while i < len(b) and j < len(a):
		if b[i] < a[j]:
			merged_arr[k] = b[i]
			i += 1
		else:
			merged_arr[k] = a[j]
			j += 1
		k += 1

	while i < len(b):
		merged_arr[k] = b[i]
		i += 1
		k += 1

	while j < len(a):
		merged_arr[k] = a[j]
		j += 1
		k += 1

	# merged_arr += a[j:]
	# merged_arr += b[i:]
	return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     # TO-DO

#     return arr

def merge_sort(arr):

	if len(arr) > 1:

		# halve the array into a LHS and RHS
		half = len(arr)//2

		# recursively call merge_sort() on LHS
		merge_sort(arr[half:])

		# recursively call merge_sort() on RHS
		merge_sort(arr[:half])

		# merge sorted pieces 

		return merge(merge_sort(arr[half:]), merge_sort(arr[:half]))

	return arr


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
