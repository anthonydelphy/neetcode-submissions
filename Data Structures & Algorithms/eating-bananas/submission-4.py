class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        result = 1
        maxElement = max(piles)
        r = maxElement

        while l<=r:
            hours = 0
            k = l+((r-l)//2)
            print(k)
            for hour in piles:
                hours += math.ceil(hour/k)
            
            print("Hours: ", hours)
            #We didnt eat all the bananas in time
            if hours > h:
                l = k+1
            # We have extra time or exactly enough time to eat the bananas
            elif hours <= h: 
                r = k-1
                result = k

    
        return result