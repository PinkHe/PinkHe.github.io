# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        # Str1 = s[0:n]
        # result = s[n:len(s)]
        # result = result + Str1
        # return result
        temp1 = ''
        temp2 = ''
        for i in range(0, n):
            temp1 += s[i]
        for i in range(n, len(s)):
            temp2 += s[i]
        return temp2 + temp1

str = 'abcdefg'
temp = Solution()
temp.reverseLeftWords(str,2)