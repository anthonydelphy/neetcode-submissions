class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l ,r = 0, len(numbers)-1
        # while l <= r:
        #     print('l=',l,'r=',r)
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1,r+1]
        #     elif numbers[l] + numbers[r] > target:
        #         r-=1
        #     else:
        #         l += 1
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            print(l,r)
            tmp = target - numbers[i]
            while l <= r:
                print(l,r)

                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
        