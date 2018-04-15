def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length = len(s)
    if length<2:
        return length
    for i in range(0,length-1):
        print i
        if s[i+1] in s[0:i+1]:
            n = s[0:i+1].index(s[i+1])
            print n,i
            str1 = s[0:i+1]
            print str1
            str2 = s[n+1:]
            print str2
            len_temp = lengthOfLongestSubstring(str2)
            if len_temp > i+1:
                return len_temp;
            else:
                return i+1
            i = i+1
    return length


#
result = lengthOfLongestSubstring("bbbbbb")
print result

# 时间复杂度太高，未通过


# 采用哈希表方法减少遍历次数时间复杂度降低。
# 其实操作思想是一样的不过每次记录start位置比切割迭代要节省时间得多
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
            # 更新完start和maxLength后重复元素的位置可以用新的位置替代！
        return maxLength
