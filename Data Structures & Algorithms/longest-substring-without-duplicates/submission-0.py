class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == ' ':
            return 1
            
        stringSet = set()
        maxSubstring = 0
        
        l,r = 0,0

        while r < len(s):
            if s[r] in stringSet:
                maxSubstring = max(maxSubstring, len(stringSet))
                stringSet = set()
                l = l +1
                r = l
                continue
                
            stringSet.add(s[r])
            r += 1

        return max(maxSubstring, len(stringSet))
            