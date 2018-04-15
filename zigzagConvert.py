def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    itemNum = numRows+1
    columns = int(len(s)/itemNum)+1
    repeatLine = int(numRows/2-1+numRows%2)
    result = ''
    if numRows%2!=0:
        for i in range(numRows):
            if i != repeatLine:
                for j in range(columns):
                    if j*itemNum+i<len(s):
                        result += s[j*itemNum+i]
                    else:break
            else:
                for j in range(columns):
                    if j*itemNum+numRows<len(s):
                        result += s[j*itemNum+i]+s[j*itemNum+numRows]
                    elif j*itemNum+i<len(s):
                        result += s[j*itemNum+i]
                    else:break
    else:
        for i in range(numRows):
            for j in range(int(len(s)/numRows)+1):
                if j*numRows+i<len(s):
                    result += s[j*numRows+i]
                else:break
    return result
s="ABCD"
result = convert(s,2)
print result
print int(2/3)+1
