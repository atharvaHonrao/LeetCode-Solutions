class Solution(object):
    def sortColors(self, nums):
        x = 0
        y = 0
        for i in range(0,len(nums)):
            if nums[i]==0 and y<len(nums) and x<len(nums):
                temp = nums[i]
                nums[i] = nums[y]
                nums[y] = nums[x]
                nums[x]=temp
                x+=1
                y+=1
            elif nums[i]==1 and y<len(nums) and x<len(nums):
                temp = nums[i]
                nums[i] = nums[y]
                nums[y] = temp
                y+=1

            
