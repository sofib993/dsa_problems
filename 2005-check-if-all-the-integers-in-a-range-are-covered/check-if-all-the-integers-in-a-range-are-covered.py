class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = []
        for i in range(left, right+1):
            arr.append(i)
        arr = set(arr)
        
        ran = []
        for start, end in ranges:
            for i in range(start, end + 1):
                ran.append(i)
        ran = set(ran)
        if arr & ran == arr:
            return True
        else:
            return False