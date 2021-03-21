def isStringPermutation(s1, s2):
    if len(s2) != len(s1): return False
    seen = {}
    for char in s1:
        seen[char] = seen[char] + 1 if char in seen else 1
    for char in s2:
        if char not in seen: return False
        seen[char] -= 1
        if seen[char] < 0: return False
    return True


'''
Complexity analysis:
  First loop (line 21-22): O(n)
      line 22: set item in dict: O(1). Complexity: O(n)*O(1) = O(n)
  Second loop (line 23-26): O(n)
      line 24: k in d in dict: O(1). Complexity: O(n)*O(1) = O(n)
      line 24: set item in dict: O(1). Complexity: O(n)*O(1) = O(n)
      line 26: get item in dict: O(1). Complexity: O(n)*O(1) = O(n)

Total Complexity: O(n)+O(n)+O(n)+O(n) = O(n)
'''


def pairsThatEqualSum(inputArray, targetSum):
    seen = set()
    ans = []
    for n in inputArray:
        complement = targetSum - n
        if complement in seen:
            ans.append((complement, n))
        seen.add(n)
    return ans


'''
Complexity analysis:
  First loop (line 63-67): O(n)
      line 64: set value: O(1). Complexity: O(n)*O(1) = O(n)
      line 65: k in d in set: O(1). Complexity: O(n)*O(1) = O(n)
      line 66: append item in list: O(1). Complexity: O(n)*O(1) = O(n)
      line 67: add item in set: O(1). Complexity: O(n)*O(1) = O(n)

Total Complexity: O(n)+O(n)+O(n)+O(n) = O(n)
'''
