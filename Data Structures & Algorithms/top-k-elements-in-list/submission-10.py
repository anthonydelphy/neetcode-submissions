class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            s[i] = s.get(i, 0) +1

        x = []
        for i in s:
            x.append([s[i],i])
        x.sort()
        res =[]
        while len(res) < k:
            res.append(x.pop()[1])

        return res