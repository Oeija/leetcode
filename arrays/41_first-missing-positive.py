class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)
        int1 = 1
        int2 = 0


        for i, x in enumerate(nums):
            if i == 0 and nums[i] > 0:
                int1 = x
                if n == 1:
                    if int1 > 1 or int1 <= 0:
                        return 1
                    else:
                        return int1+1
                    
            if x > 0 and x <= int1:
                int1 = x

            if int1 <= 0 and i == n-1:
                return 1
        
        print(int1)


        if int1 > 1:
            return 1


        for x in range(1, n+1):
            if x not in nums:
                return x
        
        if int1 == 1:
            return n+1