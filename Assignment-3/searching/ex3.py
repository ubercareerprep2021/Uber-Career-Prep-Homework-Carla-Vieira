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

# Recursive approach. Time complexity: O(log(n)). Space complexity: O(log(n)), num of recursive calls.
def pow_recursive(x, n):
    # Base case where the exponent is 0.
    if n == 0: return 1

    # If the exponent is negative, it will invert the base (from x to 1/x) and change the exponent signal to positive.
    if n < 0:
        x = 1 / x
        n = -n

    # Case which exponent is even. Calculates the value of x^(n/2) and multiply by itself.
    if n % 2 == 0:
        num = pow_recursive(x, n // 2)
        return num*num
    # Case which exponent is even.  Calculates the value of x^(n-1) and multiply by x
    else:
        return x*pow_recursive(x, n-1)

# Iterative approach. Time complexity: O(log(n)). Space complexity: O(1).
def pow_iterative(x, n):
    # If the exponent is negative, it will invert the base (from x to 1/x) and change the exponent signal to positive
    if n < 0:
        x = 1 / x
        n = -n

    # Being n = a+b, x^n = x^(a+b) = (x^a)*(x^b). So we can write n as a sum of number in the binary sequence,
    # which would be easier to calculate.
    # Ex: 2^6 = 2^(2+4) = 2^2 * 2^4 = 2^(2^1) * 2^(2^2) =  2^(0*2^0) * 2^(1*2^1) * 2^(1*2^2) * 2^(0*2^3) * ...  ->  6(decimal base) = 110(binary)
    #     3^9 = 3^(1+8) = 3^1 * 3^8 = 3^(2^0) * 3^(2^3) =  3^(1*2^0) * 3^(0*2^1) * 3^(0*2^2) * 3^(1*2^3) * ...  ->  9(decimal base) = 1001(binary)
    # For x^n = x^(a0+a1+a2+...) = x^(a0) * x^(a1) * x^(a2) * ... = x^(b0*2^0) * x^(b1*2^1) * x^(b2*2^2) * ...  ->  n(decimal base) = b0b1b2...(binary)
    # To find the binary number from a decimal base number, we usually divide this number
    # by 2 until we find 0 as quotient. The number in binary is the rest of the division by two in the order from the
    # last found to the first. So we will divide n by 2 until we find 0. When the rest of the division is 1,
    # so it means that current bit is 1, so we should multiply the answer for x^(2^(number for previous divisions of n by 2))
    # To have this value for each bit, every time we divide n by 2, we will square x as the current_product.
    ans = 1
    current_product = x

    #  In each iteration, the value of n will be divided by two and the current_product will be elevated by two.
    #  If it is odd (bit = 1), the answer will be multiplied by the current_product.
    while n > 0:
        if  n % 2 == 1:
            ans *= current_product
        current_product *= current_product
        n //= 2

    return ans

