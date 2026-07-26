class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1] * nums[-2] * nums[-3]
        m = nums[0] * nums[1] * nums[-1]

        return max(m,n)
        