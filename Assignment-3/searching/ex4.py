"""
Searching Exercise 4: Median of Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).. You may assume nums1 and nums2 cannot be both empty.

For Example:
nums1 = [1, 2], nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

# Recursive approach with binary search. Time complexity: O(log(m+n)). Space complexity: O(log(m+n), num of recursive calls.
def find_median_recursive(nums1, nums2):
    total = len(nums1) + len(nums2)

    # if it is a odd number of elements, the median is the number in the middle position
    if total % 2 == 1:
        return find_kth_recursive(nums1, nums2, total // 2)
    # if it is an even number, the median is the mean of the two middle positions
    else:
        return (find_kth_recursive(nums1, nums2, total // 2) + find_kth_recursive(nums1, nums2, total // 2 - 1)) / 2

# Recursive aux function that returns the kth element given two sorted arrays
def find_kth_recursive(nums1, nums2, k):
    # if it isn't on of the arrays, the answer is the element in the kth position of the non-empty array
    if not nums1: return nums2[k]
    if not nums2: return nums1[k]

    # gets the elements in the middle of each sorted array
    index_a, index_b = len(nums1) // 2 , len(nums2) // 2
    a, b = nums1[index_a], nums2[index_b]

    # the sum of the two middle indexes is smaller than the position wanted. As all elements in the first half of the array with the middle with smaller value with be smaller than a and b and k is bigger than index_a + index_b, we can discart this elements
    if index_a + index_b < k:
        # the value in the middle of num1 is bigger than the one in the middle of nums2. As the k position is in the second half and "a" is bigger, we know
        if a > b:
            return find_kth_recursive(nums1, nums2[index_b + 1:], k - index_b - 1)
        else:
            return find_kth_recursive(nums1[index_a + 1:], nums2, k - index_a - 1)
    # the sum of the two middle indexes is bigger than the position wanted. As all elements in the second half of the array with the middle with bigger value with be bigger than a and b and k is smaller than index_a + index_b, we can discart this elements.
    else:
        if a > b:
            return find_kth_recursive(nums1[:index_a], nums2, k)
        else:
            return find_kth_recursive(nums1, nums2[:index_b], k)


# # Recursive approach with binary search. Time complexity: O(log(m+n)). Space complexity: O(log(m+n), num of recursive calls.
# def find_median_iterative(nums1, nums2):
#     total = len(nums1) + len(nums2)
#
#     # if it is a odd number of elements, the median is the number in the middle position
#     if total % 2 == 1:
#         return find_kth_iterative(nums1, nums2, total // 2)
#     # if it is an even number, the median is the mean of the two middle positions
#     else:
#         return (find_kth_iterative(nums1, nums2, total // 2) + find_kth_iterative(nums1, nums2, total // 2 - 1)) / 2
#
# # Iterative aux function that returns the kth element given two sorted arrays
# def find_kth_iterative(nums1, nums2, k):
#
#     left1 = left2 = 0
#     right1, right2 = len(nums1)-1, len(nums2)-1
#
#     while not ((left1 > right1) or (left2 > right2)):
#         print(left1, right1, left2, right2)
#
#         # gets the elements in the middle of each sorted array
#         index_a, index_b = (right1 + left1) // 2 , (right2 + left2) // 2
#         a, b = nums1[index_a], nums2[index_b]
#
#         # the sum of the two middle indexes is smaller than the position wanted. As all elements in the first half of the array with the middle with smaller value with be smaller than a and b and k is bigger than index_a + index_b, we can discart this elements
#         if (index_a - left1) + (index_b - left2) < k:
#             # the value in the middle of num1 is bigger than the one in the middle of nums2. As the k position is in the second half and "a" is bigger, we know
#             if a > b:
#                 left2 = index_b + 1
#                 k -= (index_b - left2) + 1
#             else:
#                 left1 = index_a  + 1
#                 k -= (index_a - left1) + 1
#         # the sum of the two middle indexes is bigger than the position wanted. As all elements in the second half of the array with the middle with bigger value with be bigger than a and b and k is smaller than index_a + index_b, we can discart this elements.
#         else:
#             if a > b:
#                 right1 = index_a
#             else:
#                 right2 = index_b
#
#     print(nums1, nums2, k, left1, right1, left2, right2)
#
#     return nums2[k] if left1 > right1 else nums1[k]
