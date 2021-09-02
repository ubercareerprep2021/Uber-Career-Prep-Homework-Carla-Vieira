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

def is_in_matrix(matrix, target):
    if not matrix or not matrix[0]: return False

    n = len(matrix)-1
    m = len(matrix[0])-1

    return search_in_line(matrix, n//2, 0, m, target)

    # return is_in_limits(matrix, 0, n-1, 0, m-1, target)

def search_in_line(matrix, i, j_min, j_max, target):
    print(f"line {i} from j{j_min} to j{j_max}")

    if not (0 <= j_min <= j_max and j_max<len(matrix[0]) and 0 <= i < len(matrix)): return False

    j_mid = (j_min + j_max) // 2

    if matrix[i][j_mid] == target: return True


    if matrix[i][j_mid] > target:     # value found is bigger than target. Target can be upper or on the left
        if search_in_line(matrix, i, j_min, j_mid-1, target): return True    # Search on the left
        return search_in_column(matrix, j_mid, 0, i-1, target)               # Search upper
    else:                             # value found is smaller than target. Target can be down or on the right
        if search_in_line(matrix, i, j_mid+1, j_max, target): return True    # Search on the right
        return search_in_column(matrix, j_mid, i+1, len(matrix)-1, target)     # Search down


def search_in_column(matrix, j, i_min, i_max, target):
    print(f"col {j} from i{i_min} to i{i_max}")

    if not (0 <= i_min <= i_max and i_max<len(matrix) and 0<=j<len(matrix[0])): return False

    i_mid = (i_min + i_max) // 2

    if matrix[i_mid][j] == target: return True

    if matrix[i_mid][j] > target:     # value found is bigger than target. Target can be upper or on the left
        if search_in_column(matrix, j, i_min, i_mid-1, target): return True    # Search upper
        return search_in_line(matrix, i_mid, 0, j-1, target)                   # Search on the left
    else:                             # value found is smaller than target. Target can be down or on the right
        if search_in_line(matrix, j, i_mid+1, i_max, target): return True    # Search down
        return search_in_line(matrix, i_mid, j+1, len(matrix[0])-1, target)     # Search on the right

# def is_in_limits(matrix, i_min, i_max, j_min, j_max, target):
#
#     print(i_min, i_max, j_min, j_max)
#
#     if i_min > i_max or j_min > j_max: return False
#     if i_min == i_max and j_min == j_max: return matrix[i_min][j_min] == target
#
#     i_mid = (i_max + i_min) // 2
#     j_mid = (j_max + j_min) // 2
#
#     if matrix[i_mid][j_mid] == target:
#         return True
#     if matrix[i_mid][j_mid] > target:
#         return is_in_limits(matrix, i_min, i_mid, j_min, j_mid, target)
#     else:
#         return is_in_limits(matrix, i_mid+1, i_max, j_min, j_mid, target) or \
#                is_in_limits(matrix, i_min, i_mid, j_mid+1, j_max, target) or \
#                is_in_limits(matrix, i_mid+1, i_max, j_mid+1, j_max, target)


matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
print(is_in_matrix(matrix, 18))


class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
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

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False