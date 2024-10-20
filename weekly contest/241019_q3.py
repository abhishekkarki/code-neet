# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/description/
# Medium

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)

        maxprime = 33000
        is_prime = [True] * (maxprime)
        primes = []
        for i in range(2, maxprime):
            if is_prime[i]:
                primes.append(i)
                for j in range(i, maxprime, i):
                    is_prime[j] = False
        
        def smallestprime(num):
            for i in primes:
                if i*i > num:
                    return num
                if num % i == 0:
                    return i
        
        ops = 0
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                sp = smallestprime(nums[i])
                if sp == nums[i]:
                    return -1
                nums[i] = sp
                #print(nums)
                if nums[i] > nums[i+1]:
                    return -1
                ops += 1
        
        return ops