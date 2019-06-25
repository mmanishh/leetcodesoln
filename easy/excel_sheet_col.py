import string

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        converter = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        if n == 0 or n is None:
            return None
        ret_str = ""
        while n > 26:
            to_append = n % 26
            n = n // 26
            if to_append == 0:
                n -= 1
            ret_str = converter[to_append - 1] + ret_str
        if n > 0:
            ret_str = converter[n - 1] + ret_str
        return ret_str


if __name__ == "__main__":
    for i in range(700,800):
        print(i,Solution().convertToTitle(i))