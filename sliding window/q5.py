# https://neetcode.io/problems/sliding-window-maximum
# Hard

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        q = deque()

        for i in range(k-1):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            if not q or nums[i] <= nums[q[-1]]:
                q.append(i)
        
        res = []
        for i in range(k-1, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            if not q or nums[i] <= nums[q[-1]]:
                q.append(i)
            res.append(nums[q[0]])
            if q[0] == i-k+1:
                q.popleft()
        
        return res