class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower().replace(' ','')
        
        low = "".join(char for char in low if char.isalnum())
        print(low)
        print(math.ceil(len(low)/2))


        for i,x in enumerate(low):
            print(x,low[len(low)-1-i])
            if x == low[len(low)-1-i]:
                continue
            else:
                return False
            if i == math.ceil(len(low)/2):
                return True

        return True