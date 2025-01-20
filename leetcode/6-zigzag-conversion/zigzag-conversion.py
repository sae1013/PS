

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dic = {key: [] for key in range(0,numRows)}
        cidx = 0 
        down = 1 # 내려가고있을때 flag check
        for char in s :
            if numRows == 1 :
                dic[cidx].append(char)
                continue    
            dic[cidx].append(char)
            if down :
                cidx += 1 
            else:
                cidx -=1
            if cidx < 0 :
                cidx = 1 
                down = 1
            elif cidx > numRows-1 :
                cidx = numRows-2
                down = 0
        ans = ""
        for v in dic.values():
            for char in v :
                ans+=char
        return ans