'''
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # sign = candies[0]
        # for i in range(1,len(candies)):
        #     if candies[i] + extraCandies < sign:
        #         candies[i] = False
        #     else:
        #         sign = candies[i]
        #         candies[i] = True
        # if candies[0] + extraCandies < sign:
        #     candies[0] = False
        # else:
        #     candies[0] = True
        # return candies
        sign = candies[0]
        for i in range(1,len(candies)):
            if candies[i] > sign:
                sign = candies[i]
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= sign:
                candies[i] = True
            else:
                candies[i] = False
        return candies
            


        list1 = sorted(candies)

        print(list1)

temp = Solution()
list = [4,1,4,8,9,6,4]
print(temp.kidsWithCandies(list,1))
