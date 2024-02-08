class Solution(object):
    def sortColors(self, nums):
        index = 0
        b = False
        for i in range (0,len(nums)):
            if nums[i]==2:
                nums.append(2)
                nums[i]=-1
            if nums[i] == 1 and b == False:
                index = i
                b = True
            if nums[i] == 0:
                if b == True:
                    temp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = temp
                    index = index + 1

        while -1 in nums: 
            nums.remove(-1)
            
        
        
