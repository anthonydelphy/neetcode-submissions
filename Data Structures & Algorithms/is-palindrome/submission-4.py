class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower().replace(' ','')   
        low = "".join(char for char in low if char.isalnum())

        for i,x in enumerate(low):
            if x == low[len(low)-1-i]:
                continue
            else:
                return False
            if i == math.ceil(len(low)/2):
                return True

        return True