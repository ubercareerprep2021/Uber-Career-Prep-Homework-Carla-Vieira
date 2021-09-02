"""
Searching Exercise 1: Find Minimum
Write the code to find the minimum element in a rotated and sorted array
"""

def find_minimum(arr):
    if not arr: raise Exception("Empty array. Can not find minimum.")
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return arr[i]
    return arr[0]

def find_minimum_improved(arr):
    return binary_search(arr, 0, len(arr)-1)

def binary_search(arr, l, r):
    if l > r: raise Exception("Can not find minimum.")   # Not found. Exception control

    mid = (l + r) // 2

    if mid > 0:
        if arr[mid - 1] > arr[mid]:
            return arr[mid]
        else:
            if arr[l] > arr[mid] and arr[mid] <= arr[r]:    # peak is on the left
                print("entrou no left", arr[mid-1], "<", arr[l])
                return binary_search(arr, l, mid)
            elif arr[l] <= arr[mid] and arr[mid] > arr[r]:    # peak is on the right
                print("entrou no right", mid+1, r)
                return binary_search(arr, mid+1, r)
            else:
                print("entrou no else")
                return arr[l]
    else:
        return arr[0] if arr[0] < arr[1] else arr[1]