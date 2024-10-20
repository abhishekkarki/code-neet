# https://neetcode.io/problems/permutation-string
# Medium

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)

        for c in s1:
            counts1[c] += 1
        #print(counts1)
        l, r = 0, 0
        while r < len(s2):
            #print(l, r, s2[l], s2[r], counts2)
            if s2[r] not in counts1:
                l, r = r+1, r+1
                counts2 = defaultdict(int)
            elif r-l+1 < len(s1):
                counts2[s2[r]] += 1
                r += 1
            elif r-l+1 == len(s1):
                counts2[s2[r]] += 1
                check = True
                for char, val in counts1.items():
                    if char not in counts2 or val != counts2[char]:
                        check = False
                if check:
                    return True
                counts2[s2[l]] -= 1
                l+=1
                r += 1
        
        return False
