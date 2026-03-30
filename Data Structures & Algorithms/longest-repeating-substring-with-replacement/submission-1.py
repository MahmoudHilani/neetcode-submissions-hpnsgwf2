class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hash = {}
        res = 0
        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)
            while (r - l + 1) - max(hash.values()) > k:
                hash[s[l]] -= 1
                l += 1
                
            

            res = max(res, r - l + 1)
        return res