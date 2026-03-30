class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        
        l = 0
        for c in s1:
            hash1[c] = 1 + hash1.get(c, 0)
        curHash = hash1
        for r in range(len(s2)):
            if s2[r] in hash1 and hash1[s2[r]] > 0:
                hash1[s2[r]] -= 1
            else:
                while s2[l] is not s2[r]:
                    if s2[l] in hash1:
                        hash1[s2[l]] +=1 
                    l += 1
                l += 1
            finished = True
            for k,v in hash1.items():
                if v != 0:
                    finished = False
            if finished:
                return True
        return False

        