# binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        ll = 1
        rr = x
        ans = 0
        while ll <= rr :
            mid = (ll+rr) // 2
            if mid**2 > x :
                rr = mid-1
            else:
                ans = mid 
                ll = mid+1
        return ans 
        