"""
Sorting Exercise 2: External Sort
Given a large array containing a million entries, sort them by loading only 100 entries at a time in memory.
"""
from math import ceil
import random


def load_entries(entries):
    memory = []
    num_pages = ceil(len(entries) / 100)

    for page in range(num_pages):                  # it will take O(n/100) ~= O(n)
        memory = load_100_entries(entries[page*100:(page+1)*100], memory)

    return memory

def load_100_entries(partition,memory):
    partition.sort()                              # as .sort() takes O(nlogn), and len(partition) = 100 , this will take O(100*log100) = O(200) ~= O(1)
    memory = merge_sorted_arrays(partition, memory)
    return memory

def merge_sorted_arrays(arr1,arr2):
    i = j = 0
    arr3 = []

    while i < len(arr1) and j < len(arr2):        # it will take O(a+b), where a = len(arr1) and b = len(arr2)
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < len(arr1):                          # making sure that is no numbers left in arr1
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):                          # making sure that is no numbers left in arr2
        arr3.append(arr2[j])
        j += 1

    return arr3


# Time Complexity
# O((n/100) * (200 + (100+n)) ~= O(n^2)
# Space Complexity
# O(n)