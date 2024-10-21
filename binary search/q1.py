# https://neetcode.io/problems/eating-bananas
# Medium

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def gethour(k):
            return sum([(i-1) // k + 1 for i in piles])

        n = len(piles)
        l, r = 1,  max(piles) * len(piles) // h + 1

        while l < r:
            mid = (l + r) // 2
            #print(l, r, mid, gethour(mid))
            if gethour(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return r