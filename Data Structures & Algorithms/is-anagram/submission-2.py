class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for x in s:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1

        for y in t:
            if y in dic:
                dic[y] -= 1
            else:
                return False
        
        for x in dic:
            print(x)
            if dic[x] != 0:
                return False

        return True