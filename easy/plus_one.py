class Solution:
    def plusOne(self, digits: list) -> list:
        d =''
        digits = list(map(lambda x:str(x), digits))
        d = d.join(digits)
        
        result =list(map(lambda x:int(x),list(str(int(d)+1))))
        
        return result

if __name__ == "__main__":
    
    a = [1,2,3]
    print(Solution().plusOne(a))