# O(n^2)
class Solution(object):
    def moveZeroes(self, nums):

        for x in range(len(nums)):
            if nums[x] == 0:
                continue
            else:
                for y in range (len(nums)):
                    if nums[y] == 0 and x > y:
                        flag = nums[x]
                        nums[x] = nums[y]
                        nums[y] = flag
                        break


# O(n)
class Solution(object):
    def moveZeroes(self, nums):
        
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 