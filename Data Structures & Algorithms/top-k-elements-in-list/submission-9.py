class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            s[i] = s.get(i, 0) +1

        print(s)

        x = []
        for i in s:
            x.append([s[i],i])
        print('before',x)
        x.sort(reverse=True)
        print('after',x)
        res =[]
        while len(res) < k:
            res.append(x.pop(0)[1])

        return res