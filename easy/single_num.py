from collections import Counter 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = [k for k, v in c.items() if v == 1]

        print(res)
        return res[0]
        

if __name__ == "__main__":
    a = [1,2,1,3,2,5]
    print(Solution().singleNumber(a))