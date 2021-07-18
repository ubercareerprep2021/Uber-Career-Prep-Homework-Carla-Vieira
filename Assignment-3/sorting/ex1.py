"""
Sorting Exercise 1: Three Partition Sort
Given an Array [5, 10, 5, 20, 5, 5, 10], sort them in a single pass.
"""

""""
Obs: The method will only work as a single pass in the case that there are only up to 3 different numbers in the list 
and the chosen pivot is the middle number. Otherwise, it is not possible to say that it will sort the list correctly.
"""


def three_partition_sort(arr, pivot):
    less_than, bigger_than, equal = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            less_than.append(arr[i])
        elif arr[i] > pivot:
            bigger_than.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
    return less_than + equal + bigger_than


def specific_case():
    return three_partition_sort([5, 10, 5, 20, 5, 5, 10], 10)

# Time Complexity
# O(n)
# Space Complexity
# O(n)