from itertools import groupby

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = '1'
        for _ in range(n-1):
            out = "".join([str(len(list(g)))+k for k,g in groupby(out)])
            print(out)
            
        return out
            
        
if __name__ == "__main__":
    print(Solution().countAndSay(5))