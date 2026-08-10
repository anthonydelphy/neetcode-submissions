class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a lst of dictionaries
        # I want a list of dictionaries, with the dictionary keys storing the set and the value being the list of anagrams
        
        #Create a list
        lst = {}
        result = []
        for i in strs:
            srt = "".join(sorted(i))
            if len(lst) == 0 or srt not in lst:
                lst[srt] = [i]
                continue
            elif srt in lst:
                lst[srt].append(i)

        for i in lst:
            result.append(lst[i])

        return result