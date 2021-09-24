"""
Searching Exercise 6: Find whether an array is subset of another array
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are
not in sorted order. It may be assumed that elements in both arrays are distinct.
"""

# Using set as auxiliary data structure. Time complexity: O(m+n). Space complexity: O(n).
# This approach is recommended when is needed to prioritize time complexity other then space complexity
def isSubset1(arr1, arr2):
    elements_set = set()

    for element in arr1:
        elements_set.add(element)

    for element in arr2:
        if element not in elements_set:
            return False

    return True

# Using .sort(). Time complexity: O(m*log(m)+n*log(n)). Space complexity: O(1).
# This approach is recommended when is needed to prioritize space complexity other then time complexity
def isSubset2(arr1, arr2):

    # As python uses Tim Sort in .sort(), it will take O(n(log(n)), as n = len(arr). Both sorts together  will take
    # O(m*log(m)+n*log(n)).
    arr1.sort()
    arr2.sort()
    pointer1= pointer2 = 0

    # it will go through the arrs until one runs out
    while pointer2 < len(arr2) and pointer1 < len(arr1):
        # if the elements aren't the same, it will follow in the arr1 until it finds the correspondent (as it is sorted)
        while arr1[pointer1] != arr2[pointer2]:
            pointer1 += 1
            # if arr1 runs out it is because you can't find and arr2 element in arr1
            if pointer1 >= len(arr1):
                return False
        pointer1 += 1
        pointer2 += 1

    # if it went through the entire arr2, it is because it found all the elements of arr2. If the loop stopped
    # because of arr1, it's because it didn't find
    return pointer2 == len(arr2)