class Solution(object):
    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x 
            else:
                return True

        return False
                

       

        """
        :type nums: List[int]
        :rtype: bool
        """
        