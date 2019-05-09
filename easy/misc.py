def removeElement(nums: list, val: int) -> int:
    for index,i in enumerate(nums):
        print(index,i,val)
        if i == val:
            nums.remove(i)
    
    return len(nums),nums



if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    print(nums)
    print(removeElement(nums,2))