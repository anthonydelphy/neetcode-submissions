class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []

        for x in range(len(sortednums)-2):
            y = x+1
            z = len(sortednums)-1
            add = sortednums[x] + sortednums[y] +sortednums[z]

            while y < z:
                add = sortednums[x] + sortednums[y] +sortednums[z]
                if add > 0:
                    z -= 1
                elif add < 0:
                    y += 1
                else:
                    newVal = [sortednums[x] , sortednums[y] ,sortednums[z]]
                    if newVal not in res:
                        res.append([sortednums[x] , sortednums[y] ,sortednums[z]])
                    y+=1
                    z-=1
                    while y < z and sortednums[y] == sortednums[y - 1]:
                        y += 1
                    while y < z and sortednums[z] == sortednums[z + 1]:
                        z -= 1

        return res