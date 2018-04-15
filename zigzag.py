def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    total_len = len(s)
    if total_len<2 or numRows==1:
        return s
    item_len = 2*numRows-2
    numColumns = int(total_len/item_len)+1
    result = ''
    for i in range(numRows):
        for j in range(numColumns):
            item1_index = item_len*j+i
            if item1_index<total_len:
                result += s[item1_index]
                if i>0 and i<numRows-1:
                    item2_index = item1_index+item_len-2*i
                    if item2_index<total_len:
                        result += s[item2_index]
    return result

s = 'PAYPALISHIRING'
result = convert(s,3)
print result
