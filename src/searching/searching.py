# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if target == arr[i]:
      return i

  return -1   # not found

print(linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -6))


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while high >= low:
    mid = (low + high) // 2

    if target == arr[mid]:
      return mid
    elif arr[mid] > target:
      high = mid - 1
    elif arr[mid] < target:
      low = mid + 1

  return -1 # not found

print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 9))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
