class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = []
        s = s.lower()
        print(s)
        for i in s:
            if ord('a') <= ord(i) and ord(i) <= ord ('z'):
                sList.append(i)

            if ord('0') <= ord(i) and ord(i) <= ord ('9'):
                sList.append(i)

        print(sList)

        l,r = 0, len(sList) -1
        while l <= r:
            if sList[l] != sList[r]:
                return False
            l += 1
            r -= 1

        return True