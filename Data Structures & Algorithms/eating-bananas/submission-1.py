from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        if h == len(piles):
            return r

        def valid_rate(x: int) -> bool:
            total = 0
            for b in piles:
                total += ceil(b/x)
            return total <= h

        while l <= r:
            m = (l+r)//2
            if valid_rate(m):
                k = m
                r = m-1
            else:
                l = m+1
        
        return k