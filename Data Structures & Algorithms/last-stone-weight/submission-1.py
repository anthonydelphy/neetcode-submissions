import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) >= 2:
        #     stones.sort()
        #     largest = stones.pop()
        #     nxt = stones.pop()
        #     res = largest-nxt
        #     stones.append(res)
        # return stones[0]

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) >= 2:
            largest = heapq.heappop(stones)
            large = heapq.heappop(stones)
            res = largest-large
            heapq.heappush(stones, res)

        return -stones[0]