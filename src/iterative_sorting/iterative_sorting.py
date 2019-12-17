# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for partition in range(0, len(arr)):

	    smallest = arr[partition]

	    smallestIndex = partition

	    index = partition

	    while index != len(arr):

		    if smallest > arr[index]:

			    smallest = arr[index]

			    smallestIndex = index

		    index += 1


	    print(arr)
	    arr[partition], arr[smallestIndex] = arr[smallestIndex], arr[partition]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    swapCounter = 1

    while swapCounter != 0: 

	    swapCounter = 0

	    index = 0 

	    RHN = index + 1

	    while RHN <= len(arr)-1:

		    if arr[index] > arr[RHN]:

			    arr[index], arr[RHN] = arr[RHN], arr[index]

			    swapCounter += 1


		    index += 1

		    RHN += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr