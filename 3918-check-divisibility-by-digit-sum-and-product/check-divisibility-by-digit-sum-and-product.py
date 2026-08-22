class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr = []
        z = n
        while n > 0:
            x = n % 10
            arr.append(x)
            n = n // 10
        x = 1
        y = 0
        for i in arr:
            x *= i
            y += i
        if z % (x+y) == 0:
            return True
        else:
            return False