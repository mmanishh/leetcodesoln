class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        
        for n in set(nums):
            counter[n] =0
        
        for n in nums:
            counter[n] +=1
        
        only_once = []

        for key in counter:
            if counter[key] == 1:
                only_once.append(key)

        return only_once
        

if __name__ == "__main__":
    a = [1,2,1,3,2,5]
    print(Solution().singleNumber(a))