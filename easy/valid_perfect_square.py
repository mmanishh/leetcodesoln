'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x= num**0.5
        return float(x).is_integer()