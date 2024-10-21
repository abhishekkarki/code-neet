# https://neetcode.io/problems/minimum-window-with-characters
# Hard

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        counts = {}
        l, r = 0, 0
        res = ""
        len_res = len(s) + 1

        while r < len(s):
            if s[r] in countt:
                counts[s[r]] = 1 + counts.get(s[r], 0)
                #print("char found", l, r, s[l:r+1], counts, countt)
                included = True
                for key, val in countt.items():
                    if key not in counts or counts[key] < val:
                        included = False
                while included:
                    if r-l+1 < len_res:
                        len_res = r-l+1
                        res = s[l:r+1]
                    if s[l] in countt:
                        counts[s[l]] -= 1
                        if counts[s[l]] < countt[s[l]]:
                            included = False
                    l += 1
                    #print("found", l, r, s[l], s[r], counts, res, len_res)
            r += 1
        return res


# first worse solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        countt = defaultdict(int)
        for c in t:
            countt[c] += 1
        #print(countt)
        counts = defaultdict(int)
        l, r = 0, 0
        res = ""
        len_res = len(s) + 1
        included = False
        while r < len(s):
            #print(l, r, s[l:r+1], counts)
            if included:
                counts[s[l]] -= 1
                counts[s[r]] -= 1
                l += 1
                if r < l:
                    r += 1
                if l >= len(s):
                    break
                included = False
                continue
            if r-l+1 < len(t):
                if s[r] in countt:
                    counts[s[r]] += 1
                r += 1
                continue
            
            if s[r] in countt:
                counts[s[r]] += 1
                #print("char found", l, r, s[l:r+1], counts, countt)
                included = True
                for key, val in countt.items():
                    if key not in counts or counts[key] < val:
                        included = False
                if included == True:
                    if r-l+1 < len_res:
                        len_res = r-l+1
                        res = s[l:r+1]
                    #print("found", l, r, s[l], s[r], counts, res, len_res)
                else:
                    r += 1
            else:
                r += 1
        return res