'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    def value(self,r): 
        if (r == 'I'): 
            return 1
        if (r == 'V'): 
            return 5
        if (r == 'X'): 
            return 10
        if (r == 'L'): 
            return 50
        if (r == 'C'): 
            return 100
        if (r == 'D'): 
            return 500
        if (r == 'M'): 
            return 1000
        return -1
    
    def romanToInt(self, s: str) -> int:
        inputs = list(s)

        result = 0
        i = 0

        while i< len(s):
            # getting value of current item
            s1 = self.value(s[i])

            if i+1 < len(s):
                # getting value of next item
                s2 = self.value(s[i+1])

                # if value of current item is lesser or equal add it is
                if s1>=s2:
                    result = result + s1
                    i +=1
                # else add the next item and deduct current item
                else:
                    result = result + s2 -s1
                    i +=2

            else:
                result = result + s1
                i += 1
    
        return result