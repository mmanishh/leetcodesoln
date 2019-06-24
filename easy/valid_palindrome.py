import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        one_string = ""
        for x in s:
            if x.isalpha() or x.isdigit():
                one_string += x

        
        one_string = one_string.lower()

        print(one_string,one_string[::-1])

        if one_string == one_string[::-1]:
            return True
        else:
            return False



if __name__ == "__main__":
    

    print(Solution().isPalindrome("a race:_&cara"))