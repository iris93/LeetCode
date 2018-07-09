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
        sort2(s,i+1,end)
    else:return
def partition(s,start,end):
    i = start-1
    key = s[end] #可以看出是以最后一个元素为key的，大于key值的元素全放到i右边，小于key的元素全放到i及左边，key最后放到i+1的位置上并返回key的位置
    for j in range(start,end):
        if s[j]<=key:
            i+=1 #i+1位的元素大于key，将j位比key小的元素与之对换。
            s[i],s[j]=s[j],s[i]  #python交换不需要中间变量，因为等号右边具有更高的优先级
    s[i+1],s[end]=s[end],s[i+1]
    return i+1

# 第三种方法，利用堆栈来保存需要迭代的参数(将每次分片后的参数压入栈并循环取出)
def sort3(s,start,end):
    if start>=end:
        return
    stack = []
    stack.append(start)
    stack.append(end)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high<=low:
            continue
        # 下面与上面的分片函数基本一致，不过对返回值处理不同
        i = low-1
        key = s[high] #可以看出是以最后一个元素为key的，大于key值的元素全放到i右边，小于key的元素全放到i及左边，key最后放到i+1的位置上并返回key的位置
        for j in range(low,high):
            if s[j]<=key:
                i+=1 #i+1位的元素大于key，将j位比key小的元素与之对换。
                s[i],s[j]=s[j],s[i]  #python交换不需要中间变量，因为等号右边具有更高的优先级
        s[i+1],s[high]=s[high],s[i+1]
        stack.extend([low,i,i+2,high])


s=[3,9,5,6,7,8]
start = 0
end = len(s)-1
print end
sort3(s,start,end)
s[1],s[2]=s[2],s[1]
print s

