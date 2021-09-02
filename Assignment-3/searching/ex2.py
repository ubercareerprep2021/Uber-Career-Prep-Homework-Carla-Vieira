"""
Searching Exercise 2: Find Element
Write the code to find an element in a rotated and sorted array
"""

def find_element(arr, target):
    return binary_search(arr, 0, len(arr) - 1, target)

def binary_search(arr, left, right, target):
    if left > right: raise Exception("Can not find element.")       # Not found. Exception control

    middle = (left + right) // 2

    if target == arr[middle]: return middle

    if arr[left] < arr[middle]:
        if arr[left] <= target and target < arr[middle]:
            return binary_search(arr, left, middle-1, target)
        else:
            return binary_search(arr, middle+1, right, target)
    elif arr[middle] < arr[right]:
        if arr[middle] < target and target <= arr[right]:
            return binary_search(arr, middle+1, right, target)
        else:
            return binary_search(arr, left, middle - 1, target)

    else:
        if arr[left] == arr[middle]:
            try:
                return binary_search(arr, middle+1, right, target)
            except:
                pass
        if arr[middle] == arr[right]:
            return binary_search(arr, left, middle - 1, target)
