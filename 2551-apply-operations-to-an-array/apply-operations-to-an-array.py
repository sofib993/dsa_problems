class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i-1] * 2
                nums[i] = 0
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        return nums