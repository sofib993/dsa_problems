class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        
        cleaned = "".join(x.lower() for x in s if x.isalnum())
        return cleaned == cleaned[::-1]
        