'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif len(nums)==1:
            if target<nums[0]:
                return 0
            else:
                return 1
        else:
            for i in range(len(nums)-1):
                if target<nums[i]:
                    return i
                if nums[i]<target<nums[i+1]:
                    return i+1

            return len(nums)


if __name__ == "__main__":
    soln = Solution()

    nums = [1]

    print(soln.searchInsert(nums,0))