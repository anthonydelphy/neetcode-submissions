class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i,x in enumerate(nums):
            print(t)
            if target-x in t:
                return [t[target-x],i]
            else:
                t[x] = i
        return []

