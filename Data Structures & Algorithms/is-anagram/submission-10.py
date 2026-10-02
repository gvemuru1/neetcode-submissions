class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setT = set(t)
        sets = set(s)
        if len(s) != len(t):
            return False

        seen = {}

        for i, v in enumerate(s):
            if v in seen:
                seen[v] +=1
            else:
                seen[v] = 1

        for ch in t:
            if ch not in seen:
                return False
            
            seen[ch] -= 1


            if seen[ch] < 0:
                return False
        
        return True 

             

        