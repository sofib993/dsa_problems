from collections import Counter

class Solution:
    def isSubset(self, a, b):
        count_a = Counter(a)
        
        for num in b:
            if count_a[num] <= 0:
                return False
            count_a[num] -= 1
            
        return True
