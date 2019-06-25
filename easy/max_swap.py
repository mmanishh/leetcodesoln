class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}

        print(last)
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    print(last[d])
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num
    
    def max_swap_naive(self,num):
        A = list(map(int, str(num)))

        for i in range(len(A)):
            for j in range(1,len(A)):
                if A[i]<A[j]:
                    A[i] , A[j] = A[j] , A[i]
                    return int("".join(map(str, A)))

        return num 

if __name__ == "__main__":
    print(Solution().maximumSwap(1234))