"""
Searching Exercise 3: Implement pow(x, n)

Implement pow(x, n), which calculates x raised to the power n.

Example 3.1
Input: x = 2.0, n = 10
Output: 1024.0

Example 3.2
Input: x = 2.0, n = -2
Output: 0.25
Explanation: 2-2 ⇒ 1/(2*2) ⇒ 1/4 ⇒ 0.25
"""

def pow(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1/x

    if n % 2 == 0:
        num = pow(x, n // 2)
        return num*num
    else:
        return x*pow(x, n-1)
