class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:return ''
        
        return self.longest_prefix(strs,0,len(strs)-1)

    def longest_prefix(self,strs,l,r):

        if l==r:
            return strs[l]
        else:
            mid = (l+r)//2
            print(mid)
            lcp_left = self.longest_prefix(strs,l,mid)
            lcp_right = self.longest_prefix(strs,mid+1,r)
            print(lcp_left,lcp_right)
            return self.common_prefix(lcp_left,lcp_right)

    def common_prefix(self,left,right):

        mi = min(len(left),len(right))

        for i in range(mi):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:mi]
    
if __name__ == "__main__":
    a = ['leetcode','leet','lee','le']
    b= ['a','a','b']
    print(Solution().longestCommonPrefix(a))