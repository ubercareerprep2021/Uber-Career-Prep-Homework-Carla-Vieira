"""
Searching Exercise 2: Find Element
Write the code to find an element in a rotated and sorted array
"""

# Binary search approach. Time complexity: O(log(n)), n = len(arr) with unique elements. In worst case (many duplicates) O(n), because will need to search both sides. Space complexity: O(log(n) and wost case O(n), because of the recursive calls.
def find_element(arr, target):
    return binary_search(arr, 0, len(arr) - 1, target)

# Binary search recursive aux function.
def binary_search(arr, left, right, target):
    if left > right: raise Exception("Can not find element.")       # Not found. Exception control

    # Calculates middle num between left and right
    middle = (left + right) // 2

    # Found target
    if target == arr[middle]: return middle

    # Case which the number in middle is bigger then left, so it means the left side is sorted
    if arr[left] < arr[middle]:
        # Case which left side is sorted and the target number is inside left side. Update right value for middle-1
        if arr[left] <= target and target < arr[middle]:
            return binary_search(arr, left, middle-1, target)
        # Case which left side is sorted and the target number is not int the left side (so it is in the right side). Update left value for middle+1
        else:
            return binary_search(arr, middle+1, right, target)
    # Case which the number in middle is smaller then right, so it means the right side is sorted
    elif arr[middle] < arr[right]:
        # Case which right side is sorted and the target number is inside right side. Update left value for middle+1
        if arr[middle] < target and target <= arr[right]:
            return binary_search(arr, middle+1, right, target)
        # Case which right side is sorted and the target number is not int the right side (so it is in the left side). Update right value for middle
        else:
            return binary_search(arr, left, middle - 1, target)
    # Case which it is not possible to say whether the left or right side is correctly in ascending order (arr[middle] == arr[right] and/or arr[left] == arr[middle]).
    else:
        # If arr[left] == arr[middle], it will try to find target in the right side. If it finds it, it will return, if not, it will continues.
        if arr[left] == arr[middle]:
            try:
                return binary_search(arr, middle+1, right, target)
            except:
                pass
        # If arr[middle] == arr[right], it will try to find target in the left side. If it finds it, it will return, if not, it will raise the not found exception.
        if arr[middle] == arr[right]:
            return binary_search(arr, left, middle - 1, target)
