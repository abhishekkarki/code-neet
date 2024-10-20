# https://neetcode.io/problems/spiral-matrix
# Medium

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n-1, 0, m-1

        direc = 'r'
        res = []
        while l <= r and t <= b:
            if direc == 'r':
                #print("start", direc)
                for j in range(l, r+1):
                    res.append(matrix[t][j])
                direc = 'd'
                t += 1
                #print(res)
            elif direc == 'd':
                #print("start", direc)
                for j in range(t, b+1):
                    res.append(matrix[j][r])
                direc = 'l'
                r -= 1
                #print(res)
            elif direc == 'l':
                #print("start", direc)
                for j in range(r, l-1, -1):
                    res.append(matrix[b][j])
                direc = 'u'
                b -= 1
                #print(res)
            elif direc == 'u':
                #print("start", direc)
                for j in range(b, t-1, -1):
                    res.append(matrix[j][l])
                direc = 'r'
                l += 1
                #print(res)
        return res