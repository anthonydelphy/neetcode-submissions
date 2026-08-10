class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a lst of dictionaries
        # I want a list of dictionaries, with the dictionary keys storing the set and the value being the list of anagrams
        
        #Create a list
        lst = {}
        for i in strs:
            srt = "".join(sorted(i))
            if srt in lst:
                lst[srt].append(i)
                continue
            lst[srt] = [i]
            
        return list(lst.values())