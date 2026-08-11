class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []
        #print(sortednums)

        for x,i in enumerate(sortednums):
            if x >= len(sortednums)-2:
                break
            y = x+1
            z = len(sortednums)-1
            add = sortednums[x] + sortednums[y] +sortednums[z]
            #print(x,y,z,'lookie here')
            #print(sortednums[x] , sortednums[y] ,sortednums[z],add)
            while y < z:
                #print(sortednums[x] , sortednums[y] ,sortednums[z],add)
                add = sortednums[x] + sortednums[y] +sortednums[z]

                if add > 0:
                    z -= 1
                elif add < 0:
                    y += 1
                else:
                    #print('Hit!')
                    newVal = [sortednums[x] , sortednums[y] ,sortednums[z]]
                    if newVal not in res:
                        res.append([sortednums[x] , sortednums[y] ,sortednums[z]])
                    y+=1

        return res