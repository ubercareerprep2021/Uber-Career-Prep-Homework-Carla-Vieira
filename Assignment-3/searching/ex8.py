"""
Searching Exercise 8: Bonus Question
Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k.


"""
from collections import defaultdict

# Time complexity: O(n). Space complexity: O(k).
def count_distinct_elements(arr, k):
    # the dict current_elements will have the as keys the current elements and as values the current number of
    # occurrences of that element
    current_elements = defaultdict(int)

    ans = []

    # it wil pass thought the arr, adding the elements to the dict. if exceeded the window limit, it eliminates the
    # initial element. for each window, add the amount of unique elements at the moment
    for index, element in enumerate(arr):
        if index >= k:
            discard_element = arr[index-k]
            current_elements[discard_element] -= 1
            if current_elements[discard_element] == 0:
                current_elements.pop(discard_element)

        current_elements[element] += 1

        if index >= k-1:
            ans.append(len(current_elements))

    return ans
