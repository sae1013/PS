# 갯수 비교
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(int)
        for x in s : 
            table[x] += 1
        
        for x in t :
            table[x] -= 1 
        
        for _,v in table.items() : 
            if v is not 0 :
                return False
        return True