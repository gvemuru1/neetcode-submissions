class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            countKey = [0]* 26
            for c in s:
                countKey[ord(c)- ord("a")] +=1 
            
            res[tuple(countKey)].append(s)

        return list(res.values())