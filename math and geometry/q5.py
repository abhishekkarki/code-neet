# https://neetcode.io/problems/multiply-strings
# Medium

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                res[i+j] += mul
                k = i+j
                while res[k] >= 10:
                    res[k+1] += res[k] // 10
                    res[k] = res[k] % 10
                    k += 1
                print(num1[i], num2[j], res)
        str_res = ''
        start = False
        for d in res[::-1]:
            if d != 0:
                start = True
            if start:
                str_res += str(d)
        return str_res