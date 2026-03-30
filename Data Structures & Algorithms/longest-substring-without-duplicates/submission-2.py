class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLet = 0
        chars = []
        for r in range(len(s)):
            if s[r] in chars:
                while chars and chars[0] != s[r]:
                    chars.pop(0)
                if chars:
                    chars.pop(0)
            chars.append(s[r])

            maxLet = max(maxLet, len(chars))
        return maxLet