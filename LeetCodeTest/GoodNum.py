# 给你一个整数数组 nums 。

# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

# 返回好数对的数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-good-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 0
        for i in range(0,len(nums)):
            sign_01 = 0
            for j in range(i+1,len(nums)):

                if nums[i] == nums[j]:
                    sign = sign + 1
        return sign

list = Solution()
nums = [1,2,3,1,1,3]
print(list.numIdenticalPairs(nums)) 


