# https://neetcode.io/problems/course-schedule
# Medium

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        cmap = {}
        cset = set()

        for c1, c2 in prerequisites:
            #print(c1, c2, cmap)
            if c1 not in cmap:
                cmap[c1] = [c2]
            else:
                cmap[c1].append(c2)
            cset.add(c1)
            cset.add(c2)
        #print(cmap, cset)
        visited = set()
        canfinish = set()

        def dfs(c1):
            #print("before", c1, visited, canfinish)
            if c1 in canfinish: return True
            if c1 in visited: return False
            visited.add(c1)
            if c1 not in cmap:
                canfinish.add(c1)
                return True
            for c2 in cmap[c1]:
                if not dfs(c2):
                    print("in", c1, c2, False)
                    return False
            canfinish.add(c1)
            return True
        
        for c in cset:
            if not dfs(c):
                return False
        
        return True