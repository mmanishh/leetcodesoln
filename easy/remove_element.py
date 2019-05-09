"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        for j in range(0,len(nums)):
            print(i,j)
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
            
    
        return i



if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    soln = Solution()
    print(soln.removeElement(nums,2))