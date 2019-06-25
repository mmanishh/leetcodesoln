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
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        alphas = list(string.ascii_uppercase)
        alphas_dict = {v:i+1 for i,v in enumerate(alphas)}

        value = 0
        for i in range(len(s)):
            if i==len(s)-1:
                value+=alphas_dict[s[i]]
            else:
                value +=26 ** (len(s)-1-i)*alphas_dict[s[i]]
        
        return value



if __name__ == "__main__":
    # for i in range(25,1000):
    #     print(i,Solution().convertToTitle(i),Solution().titleToNumber(Solution().convertToTitle(i)))

    print(Solution().titleToNumber('BA'))