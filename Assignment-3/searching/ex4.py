"""
Searching Exercise 4: Median of Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).. You may assume nums1 and nums2 cannot be both empty.

For Example:
nums1 = [1, 2], nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

def find_median(nums1, nums2):
    total = len(nums1) + len(nums2)

    if total % 2 == 1:
        return find_kth(nums1, nums2, total // 2)
    else:
        return (find_kth(nums1, nums2, total // 2) + find_kth(nums1, nums2, total // 2 - 1)) / 2

def find_kth(nums1, nums2, k):
    if not nums1: return nums2[k]
    if not nums2: return nums1[k]

    index_a, index_b = len(nums1) // 2 , len(nums2) // 2
    a, b = nums1[index_a], nums2[index_b]

    if index_a + index_b < k:
        if a > b:
            return find_kth(nums1, nums2[index_b+1:], k - index_b - 1)
        else:
            return find_kth(nums1[index_a + 1:], nums2, k - index_a - 1)
    else:
        if a > b:
            return find_kth(nums1[:index_a], nums2, k)
        else:
            return find_kth(nums1, nums2[:index_b], k)
