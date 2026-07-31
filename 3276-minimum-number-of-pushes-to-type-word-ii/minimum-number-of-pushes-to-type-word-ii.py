class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sr = sorted(counts.values(), reverse=True)
        result = 0
        
        for i in range(len(sr)):
            x = ((i // 8) + 1) * sr[i]
            result += x
        return result