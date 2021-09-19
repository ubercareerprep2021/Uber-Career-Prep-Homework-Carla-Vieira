"""
Searching Exercise 1: Find Minimum
Write the code to find the minimum element in a rotated and sorted array
"""

# Iterative approach. Time complexity: O(n), n = len(arr). Space complexity: O(1).
def find_minimum_iterative(arr):
    if not arr: raise Exception("Empty array. Can not find minimum.")    # Empty array. Exception control

    # It will go through the entire array until it finds the number which the previous one is greater than it (find a peak) and return it.
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return arr[i]

    # If not found, it is because all numbers are equal or the smallest number is first. In these two cases, return the first number.
    return arr[0]

# Binary search approach. Time complexity: O(log(n)), n = len(arr). Space complexity: O(1).
def find_minimum_binary_search(arr):
    if not arr: raise Exception("Empty array. Can not find minimum.")  # Empty array. Exception control
    if len(arr) == 1: return arr[0]                                    # Array with one number.

    left = 0
    right = len(arr)-1

    # Case where the smallest number is first. Return first
    if arr[right] > arr[0]:
        return arr[0]

    # Do the binary search until find the peak
    while right >= left:

        # Calculates middle num between left and right
        mid = (left + right) // 2

        # Check with peak is between the mid and the next number. If yes, return the next number as the minimum number.
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]

        # Check with peak is between the previous number and mid. If yes, return mid as the minimum number.
        if arr[mid-1] > arr[mid]:
            return arr[mid]

        # If the number in the mid index is bigger than the first number, so the peak is on the right half and the left index should be updated to mid +1. If it is less than or equal, index right should be updated.
        if arr[mid] > arr[0]:
            left = mid + 1
        else:
            right = mid - 1

    # Peak not found, all numbers are equal. Return the first number.
    return arr[0]
