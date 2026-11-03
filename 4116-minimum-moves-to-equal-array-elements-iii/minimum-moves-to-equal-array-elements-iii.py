class Solution:
    def minMoves(self, nums: List[int]) -> int:
        g = max(num for num in nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] < g:
                count += g - nums[i]
        return count