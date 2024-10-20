# https://neetcode.io/problems/count-squares
# Medium

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        #print(point)
        #print(self.ptsCount)
        keys_list = list(self.ptsCount.keys())
        for i in keys_list:
            if i[0] == point[0] or i[1] == point[1]: continue
            #print((i[0], point[1]), (i[1], point[0]))
            if (i[0], point[1]) in self.ptsCount and (point[0], i[1]) in self.ptsCount:
                res += self.ptsCount[i] * self.ptsCount[(i[0], point[1])] * self.ptsCount[(point[0], i[1])]
            #print(i, res)
        return res