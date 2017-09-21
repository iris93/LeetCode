
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlist = []
        substring = ''
        for item in s:
            if item not in substring:
                substring= substring+item
            else:
                strlist.append(substring)
                itemindex = substring.find(item)
                strlist.append(substring[0:itemindex])
                substring= substring[itemindex+1:]+item
        strlist.append(substring)
        maxlength = 0
        for item in strlist:
            if len(item) > maxlength:
                maxlength = len(item)
        return maxlength
                