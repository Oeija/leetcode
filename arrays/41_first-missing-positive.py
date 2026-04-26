class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)

        for x in range(n):
            while 1 <= nums[x] <= n and nums[nums[x] - 1] != nums[x]:
                # swap nums[i] into its correct position
                correct_idx = nums[x] - 1
                nums[x], nums[correct_idx] = nums[correct_idx], nums[x]

        for x in range(n):
            if nums[x] != x + 1:
                return x + 1

        return n + 1