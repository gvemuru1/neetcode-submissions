class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mapu = {}
        if len(s) != len(t):
            return False

        for c in s:
            if c not in mapu:
                mapu[c] = 1
            else:
                mapu[c] += 1

        for ch in t:
            if ch not in mapu:
                return False
            else: 
                mapu[ch] -= 1

            if mapu[ch] < 0:
                return False
            
        return True

        
        