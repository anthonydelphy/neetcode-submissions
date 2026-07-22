class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            print(s)
            for i in s:
                print(ord(i)-ord('a'))
                arr[ord(i) - ord('a')] += 1

            listSet = tuple(arr)
            print(listSet)
            dict[listSet].append(s)
        
        print(dict.values())
        return dict.values()