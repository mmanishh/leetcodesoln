"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums)==0:
            return 0
        i = 0
        
        for j in range(1,len(nums)):
            if nums[j] !=nums[i]:
                i+=1
                nums[i] = nums[j]

            print(nums)
        
        return i+1,nums


if __name__ == "__main__":
    nums = [0,0,1,1,2]

    solution = Solution()
    print(solution.removeDuplicates(nums))