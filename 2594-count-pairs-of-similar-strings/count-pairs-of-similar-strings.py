class Solution:
    def similarPairs(self, words: List[str]) -> int:

        words = [set   (w) for w in words]          
        words = [sorted(w) for w in words]          
        words = [tuple (w) for w in words]          

        c = Counter(words)                          
        
        return  sum(n*(n-1) for n in c.values())//2 