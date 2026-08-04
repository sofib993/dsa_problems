class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start, end = min(nums), max(nums)
        
        num_set = set(nums)
        
        return [i for i in range(start, end + 1) if i not in num_set]
