"""
Sorting Exercise 5: Peaks and Valleys
In an array of integers, a "peak" is an element that is greater than or equal to the adjacent integers and a "valley" is
an element that is less than or equal to the adjacent integers. For example, in the array [5, 8, 6, 2, 3, 4, 6], [8, 6]
are peaks and [5, 2] are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and
valleys.

Example
Input: [5, 3, 1, 2, 3]
Output: [5, 1, 3, 2, 3]
"""

def sort_peaks_and_valleys(arr):
    for i in range(1, len(arr)-1):

        if arr[i-1] > arr[i]:        # in case previous number is bigger than current
            if arr[i+1] < arr[i]:    # in case next number is smaller than current (so it is wrong and we should change current with next)
                arr[i], arr[i+1] = arr[i+1], arr[i]

        else:                        # in case previous number is smaller than current
            if arr[i+1] > arr[i]:    # in case next number is bigger than current (so it is wrong and we should change current with next)
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# Time Complexity
# O(n)
# Space Complexity
# O(1)