# https://neetcode.io/problems/pow-x-n
# Medium

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow2(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = pow2(x * x, n // 2)
            return x * res if n % 2 else res
        
        res = pow2(x, abs(n))

        return res if n >= 0 else 1 / res