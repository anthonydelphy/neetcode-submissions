class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        containsZero = False
        zeroCount = 0
        for i in nums:
            if i == 0:
                containsZero = True
                zeroCount += 1
            else:
                allZeros = False
                x *= i

        print(x)
        if len(nums) == zeroCount or zeroCount >1:
            return [0] * len(nums)
                
        result = [x] * len(nums)
        for i in range(len(result)):
            if nums[i] != 0 and not containsZero:
                result[i] = result[i] // nums[i]
            elif nums[i] != 0 and containsZero:
                result[i] = 0

   




        return result