"""
Searching Exercise 5: Search value in mxn Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

For Example, consider the following matrix:
[ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]

Target  = 5, Return value = true
Target = 20. Return value = false
"""

# Binary search approach. Time complexity: O(min(m,n)*(log(n)+log(m))), as each diagonal takes O(log(n)+long(m)) and
# worst case scenario it will search for min(m,n) diagonals. Space complexity: O(1)
def is_in_matrix(matrix, target):
    # If matrix is empty: it won't have the target.
    if not matrix or not matrix[0]:
        return False

    # Iterate over matrix diagonals starting from matrix[0][0] until matrix[min(m,n)][min(m,n)]. If find target stop
    # and return
    for i in range(min(len(matrix), len(matrix[0]))):
        # Look if target is in the right of the current diagonal
        vertical_found = matrix_binary_search(matrix, target, i-1, True)
        # Look if target is below the current diagonal
        horizontal_found = matrix_binary_search(matrix, target, i-1, False)
        # If target is the diagonal or is in the right or below the diagonal, target found
        if matrix[i][i]==target or vertical_found or horizontal_found:
            return True

    return False

# Time complexity: O(log(a)), where a is n or m
def matrix_binary_search(matrix, target, start, is_vertical):
    lo = start
    hi = len(matrix[0]) - 1 if is_vertical else len(matrix) - 1

    while hi >= lo:
        mid = (lo + hi) // 2
        if is_vertical:  # searching a column
            if matrix[start][mid] < target:
                lo = mid + 1
            elif matrix[start][mid] > target:
                hi = mid - 1
            else:
                return True
        else:  # searching a row
            if matrix[mid][start] < target:
                lo = mid + 1
            elif matrix[mid][start] > target:
                hi = mid - 1
            else:
                return True

    return False
