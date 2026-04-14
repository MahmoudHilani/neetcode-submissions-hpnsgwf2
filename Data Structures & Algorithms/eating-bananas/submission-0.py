class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, k = 1, max(piles)
        while l <= k:
            mid = (k + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                l = mid + 1
            else:
                k = mid - 1
        return l
