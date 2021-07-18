"""
Sorting Exercise 3: Sorted Merge
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order in one pass and using O(1) space.
"""

def merge_sorted_arrays(A, B, size_A):
    pointer_A = size_A - 1
    pointer_B = len(B) - 1
    i = len(A)-1

    while pointer_A >=0 and pointer_B >=0:
        if A[pointer_A] >= B[pointer_B]:
            A[i] = A[pointer_A]
            pointer_A -= 1
            i -= 1
        else:
            A[i] = B[pointer_B]
            pointer_B -= 1
            i -= 1

    while pointer_B >=0:     # in the case that are still missing numbers in B, we need to make sure we passed all numbers to A
        A[i] = B[pointer_B]
        pointer_B -= 1
        i -= 1

    return A

# Time Complexity
# O(a+b)
# Space Complexity
# O(1)
