class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = {}
        res = []
        for i,num in enumerate(nums):
            hash[num] = i
        for j in range(len(nums) -1 ):
            for k in range(j + 1, len(nums)):
                target = -nums[j]-nums[k]
                if target in hash and sorted([nums[j],nums[k],target]) not in res and hash[target] > k:
                    res.append(sorted([nums[j],nums[k],target]))
        return res
