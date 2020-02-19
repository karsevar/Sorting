# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for index in range(0, len(arr)):
    if arr[index] == target:
      return index

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  
  # create a loop:
  while high >= low:

  # start with the middle index:
    middlepoint = (low + high) // 2

  # if middle index is equal to target return index 
    if arr[middlepoint] == target:
      return middlepoint
  # else check if middle point is larger than target return Right hand side 
    else:
      if arr[middlepoint] > target:
        high = middlepoint - 1
  # else return left hand side 
      elif arr[middlepoint] < target:
        low = middlepoint + 1 

  return -1 # not found

print(binary_search([1,2,3,4], 5))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  # base case:
  if arr[middle] == target:
    return middle 
  elif low > high:
    return -1
  else:
    #recursive case
    if arr[middle] > target:
      high = middle - 1
      return binary_search_recursive(arr, target, low, high) 
    elif arr[middle] < target:
      low = middle + 1 
      return binary_search_recursive(arr, target, low, high)

print(binary_search_recursive([1,2,3,4], 5, 0, 3))
