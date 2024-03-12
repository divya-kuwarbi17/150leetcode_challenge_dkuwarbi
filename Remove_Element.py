class Solution:
    def removeElement(self,nums:List[int], val: int) -> int:
        count = 0
        i = 0
        j = 0
        while i <len(nums) and j<len(nums):
            # print(f"{i}---->{nums}")
            if nums[i]==val :
                if i<len(nums)-count:
                    a = nums.pop(i)
                    nums.append(a)
                    count = count +1
                    # print("I'm count")
                    j = j+1
                else:
                    i = i+1
                    count = count+1
                    j = j+1
                    # print("I'm count")
                                    
            else:
                i=i+1
                j= j+1
        sd =len(nums)-count
        nums[:] = nums[:sd]
        # print(nums)

        return int(sd)
