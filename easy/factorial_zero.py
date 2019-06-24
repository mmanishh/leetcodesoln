from collections import Counter
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0
        x=0
        while n != 0:
            x += n // 5
            n //= 5
            print(x,n)
            
        return x

    def factorial(self,n):
        fact = 1
        for i in reversed(range(1,n+1)):
            fact = fact*i
        
        return fact



if __name__ == "__main__":
    print(Solution().trailingZeroes(10))