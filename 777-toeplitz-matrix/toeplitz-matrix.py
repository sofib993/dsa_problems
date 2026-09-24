class Solution:
    def isToeplitzMatrix(self, m: list[list[int]]) -> bool:
        for i in range(len(m) - 1):
            for j in range(len(m[i]) - 1):
                if m[i][j] != m[i+1][j+1]:
                    return False
        return True