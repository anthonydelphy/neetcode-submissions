class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}

        for i in nums:
            x[i] = x.get(i,0) + 1

        s = []

        for num, cnt in x.items():
            s.append([cnt,num])
        s.sort()

        print(s)

        result = []
        while len(result) < k:
            result.append(s.pop()[1])

        return result