class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sr = sorted(counts.values(), reverse=True)
        result = 0
        
        for i, sr in enumerate(sr):
            x = ((i // 8) + 1) * sr
            result += x
        return result