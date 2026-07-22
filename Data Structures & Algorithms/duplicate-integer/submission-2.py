class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = {}

        for x,y in enumerate(nums):
            
            if y in t:
                return True
            else:
                t[y] = x
            


        print(nums)
        print(t)

        return False