"""
Searching Exercise 7: Given an array A[] and a number x, check for pair in A[] with sum as x
Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two
elements in A whose sum is exactly x.
"""

# Using set as auxiliary data structure. Time complexity: O(n). Space complexity: O(n).
# This approach is recommended when is needed to prioritize time complexity other then space complexity
def is_pair_with_sum1(A, x):
    # Creates a set to store the complements needed to a number can sum to x.
    complements = set()

    # for every element in the array, it will check if the element is a complement of a posterior checked number, if
    # yes, pair founded, if not, its complement wil be added to the set
    for element in A:
        if element in complements:
            return True
        complements.add(x-element)

    return False

# Using .sort(). Time complexity: O(n*log(n)). Space complexity: O(1).
# This approach is recommended when is needed to prioritize space complexity other then time complexity
def is_pair_with_sum2(A, x):
    # As python uses Tim Sort in .sort(), it will take O(n(log(n)), as n = len(arr)
    A.sort()

    left, right = 0, len(A)-1

    while left<right:
        if A[left] + A[right] == x:
            return True
        elif A[left] + A[right] < x:
            left += 1
        else:
            right -= 1

    return False