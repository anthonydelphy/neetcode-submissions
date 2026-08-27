class Solution:
    def eatBananas(self, piles, speed):
            result = 0
            for i in piles:
                result += -(-i//speed) #Trick to CEIL math
            return result
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = result = 1
        while l <= r:
            speed = l +((r-l)//2)
            if self.eatBananas(piles,speed) <= h:
                result, r = speed, speed-1
            else:
                l = speed+1

        return result
