class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(idx, num):
            l, r = idx, len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == num:
                    return mid
                elif numbers[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        for i in range(len(numbers)):
            res = binarySearch(i, target - numbers[i])
            if res != -1 and i != res:
                return [i + 1, res + 1]
        
