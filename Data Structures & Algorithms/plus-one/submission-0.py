class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(len(digits))
        s = ''
        for x in digits:
            s += str(x)
        
        s = str(int(s)+1)
        print(s)
        result = []
        for x in s:
            result.append(int(x))
        return result