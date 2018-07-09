#conding:utf-8
# 这里复写一下快速排序
#快速排序的时间复杂度为：O(nlogn)

# 这种方法是最常见的，原地排序，递归方法实现，注意递归的结束条件。
def sort1(s,start,end):
    if start>end:
        return
    key=s[start]
    i = start
    j = end
    while i<j:
        while i<j and key < s[j]:
            j=j-1
        s[i]=s[j]
        while i<j and key >= s[i]:
            i=i+1
        s[j]=s[i]
    s[i]=key
    sort1(s,start,i-1)
    sort1(s,i+1,end)



#学习第二种快速排序实现方法 
def sort2(s,start,end):
    if start<end:
        i = partition(s,start,end)
        sort2(s,start,i-1)
        sort2(i+1,end)
    else:return
def partition(s,start,end):
    i = start-1
    key = s[end] #可以看出是以最后一个元素为key的，大于key值的元素全放到i右边，小于key的元素全放到i及左边，key最后放到i+1的位置上并返回key的位置
    for j in range(start,end):
        if s[j]<=key:
            i+=1 #i+1位的元素大于key，将j位比key小的元素与之对换。
            s[i],s[j]=s[j],s[i]
    s[i+1],s[end]=s[end],s[i+1]
    return i+1

    
s=[3,9,5,6,7,8]
start = 0
end = len(s)-1
print end
sort2(s,start,end)
print s
