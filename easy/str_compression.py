from itertools import groupby

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = list(sum([(k,str(len(list(g)))) for k,g in groupby(chars)],()))

        return result

if __name__ == "__main__":
    print(Solution().compress(["a","a","b","b","c"]))