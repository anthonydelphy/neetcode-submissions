class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = defaultdict(int)
        l = r = result = 0
        while r < len(s):
            test[s[r]] += 1
            while test[s[r]] > 1:
                test[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result