class Solution(object):
    def majorityElement(self, nums):

        unique = list(set(nums))

        temp = [nums.count(x) for x in unique]

        biggest = max(temp)
        index = temp.index(biggest)

        value = unique[index]
        
        return value