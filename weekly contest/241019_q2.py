# https://leetcode.com/contest/weekly-contest-420/problems/count-substrings-with-k-frequency-characters-i/submissions/1427860032/
# Medium

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)

        l, r = 0, 0
        cdict = {s[r] : 1}
        
        res = 0
        while r < n:
            #print("start", r, cdict)
            if max(cdict.values()) >= k:
                res += n-r
                #print(l, r, res, s[l:r+1], cdict)
                if cdict[s[l]] == 1:
                    del cdict[s[l]]
                else:
                    cdict[s[l]] -= 1
                l += 1
                if r < l:
                    r += 1
                    if r < n:
                        if s[r] in cdict:
                            cdict[s[r]] += 1
                        else:
                            cdict[s[r]] = 1
                        
                #print(cdict, l, r)
            else:
                r += 1
                #print("skipped", r, cdict)
                if r < n:
                    if s[r] in cdict:
                        cdict[s[r]] += 1
                    else:
                        cdict[s[r]] = 1
        return res