class Solution:
    def eatBananas(self, piles, speed):
            result = 0
            for i in piles:
                result += -(-i//speed) #Trick to CEIL math
            return result
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        print(piles,l,r)
        result = 1
        while l <= r:
            speed = l +((r-l)//2)
            k = self.eatBananas(piles,speed)
            print('k',k,'speed',speed)
            if k <= h:
                result = speed
                r = speed-1
                
            else:
                l = speed+1

        return result
