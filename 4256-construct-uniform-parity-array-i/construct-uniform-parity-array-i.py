class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_count = sum(1 for x in nums1 if x % 2 != 0)
        
        # We can make all even if odd_count != 1
        # We can make all odd if odd_count >= 1
        return (odd_count != 1) or (odd_count >= 1)
