
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    maxlen = 1
    totallen = len(s)
    start = 0
    for i in range(totallen):
        if i-maxlen>=1 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]:
            start = i-maxlen-1
            maxlen+=2

            continue
        if i-maxlen>=0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]:
            start = i-maxlen
            maxlen +=1
    return s[start:start+maxlen]





s='abbac'
# print s[::-1]

result = longestPalindrome(s)
print result
