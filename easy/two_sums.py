'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        
        for i in range(len(nums)):
            
            x= target - nums[i]
            if x in nums and nums.index(x)!=i:
                return [i,nums.index(x)]