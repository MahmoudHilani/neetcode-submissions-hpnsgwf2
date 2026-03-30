class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        hash1 = {}
        strHash = {}
        l = 0
        res, resLen = [-1,-1], float("infinity")
        for i in range(len(t)):
            if t[i] in hash1:
                hash1[t[i]] += 1
            else:
                hash1[t[i]] = 1
        need = len(hash1)
        have = 0
        for r in range(len(s)):
            strHash[s[r]] = 1 + strHash.get(s[r], 0)
            if s[r] in hash1 and hash1[s[r]] == strHash[s[r]]:
                have += 1
            while have == need:
                if resLen > r-l+1:
                    res = [l, r]
                    resLen = r-l+1
                strHash[s[l]] -= 1
                if s[l] in hash1 and hash1[s[l]] > strHash[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("Infinity") else ""
                
