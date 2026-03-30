class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        maxLen = 0
        curLen = 0
        for i, num in enumerate(nums):
            hash[num] = i
        
        for numb in hash:
            if numb - 1 not in hash:
                idx = numb
                curLen = 1
                while idx + 1 in hash:
                    curLen += 1
                    idx += 1
            if curLen > maxLen:
                maxLen = curLen
        return maxLen