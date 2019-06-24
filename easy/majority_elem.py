from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        counter = dict(counter)

        for k in counter:
            if counter[k] > len(nums)/2:
                return k
        
if __name__ == "__main__":
    print(Solution().majorityElement([1,1,1,2,3,3,3,3,3]))