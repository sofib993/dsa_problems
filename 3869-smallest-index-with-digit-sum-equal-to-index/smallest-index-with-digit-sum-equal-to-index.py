class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = 0
            x = nums[i]
            while x > 0:
                s += x % 10
                x = x // 10
            if s == i:
                return i
        return -1
