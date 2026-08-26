class Solution:
    def eatingBananas(self,piles, speed) -> int:
        result = 0
        for i in piles:
            result += math.ceil(float(i)/speed)
        return result
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l,r = 1, max(piles)
        print(l,r)
        while l <= r:
            m = l+ ((r-l)//2)
            hoursTook = self.eatingBananas(piles,m)
            if hoursTook > h:
                l = m+1
            elif hoursTook <= h:
                k = m
                r = m-1

        return k

