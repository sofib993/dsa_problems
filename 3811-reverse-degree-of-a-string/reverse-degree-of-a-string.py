class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i,c in enumerate(s):
            r = 26 - (ord(c) - 97)
            total += r * (i+1)
        return total