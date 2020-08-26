class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sign = 0
        # for i in range(0,len(nums)):
        #     nums[i] = nums[i] + sign
        #     sign = nums[i]
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]


list = [1,2,3,4,5]
test = Solution()

test.runningSum(list)
print(list)