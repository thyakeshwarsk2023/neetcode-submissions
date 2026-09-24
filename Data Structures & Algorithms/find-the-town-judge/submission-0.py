class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inn = [0] * (n +1)
        out = [0] * (n+1)

        for a , b in trust:
            out[a] += 1
            inn[b] += 1

        for person in range(1, n+1):
            if out[person] == 0 and inn[person] == n -1 :
                return person

        return -1        