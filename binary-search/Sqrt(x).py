Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

# can be used for any q involving squares etc.. 
# Eg ---> Valid perfect square question

class Solution(object):
    def mySqrt(self, x):

        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid  < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
