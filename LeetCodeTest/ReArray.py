class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # result = []
        # result1 = nums[0:n]
        # result2 = nums[n:len(nums)]
        # j,k = 0,0
        # for i in range(0,len(nums)):
        #     if i % 2 == 0:
        #         result.append(result1[j])
        #         j = j + 1
        #     else:
        #         result.append(result2[k])
        #         k = k + 1
        # return result
        


    

temp = Solution()

list = [1,2,3,4]

print(temp.shuffle(list,2))
