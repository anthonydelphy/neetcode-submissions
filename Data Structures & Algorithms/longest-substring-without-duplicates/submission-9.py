class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==1:
            return 1
        
        test = defaultdict(int)
        result = 0
        l,r = 0,0
        while r < len(s):
            #print(l,r,s[l],s[r])
            test[s[r]] += 1
            while test[s[r]] > 1: 
                test[s[l]] -=1
                l+=1
            #print(test)
            result = max(result,r-l+1)
            r +=1
        return result
            
