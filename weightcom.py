#coding:utf-8
# 这是网易的笔试题，应该主要是考察二叉树
# 小明陪小红去看钻石，他们从一堆钻石中随机抽取两颗并比较她们的重量。这些钻石的重量各不相同。在他们们比较了一段时间后，它们看中了两颗钻石g1和g2。现在请你根据之前比较的信息判断这两颗钻石的哪颗更重。

# 给定两颗钻石的编号g1,g2，编号从1开始，同时给定关系数组vector,其中元素为一些二元组，第一个元素为一次比较中较重的钻石的编号，第二个元素为较轻的钻石的编号。最后给定之前的比较次数n。请返回这两颗钻石的关系，若g1更重返回1，g2更重返回-1，无法判断返回0。输入数据保证合法，不会有矛盾情况出现。

# 测试样例：
# 2,3,[[1,2],[2,4],[1,3],[4,3]],4
# 返回: 1

class Cmp:
    # 这种方法是我最先想出来的，无奈超时了。
    def cmp(self, g1, g2, records, n):
        # write code here
        g1b=[g1]
        g1s=[g1]
        tags = []
        while n:
            
            for i in range(len(records)):
                # print tags
                if i in tags:
                    # print i
                    continue
                elif records[i][0] in g1s :
                    g1s.append(records[i][1])
                    tags.append(i)
                    n = n-1
                elif records[i][1] in g1b:
                    g1b.append(records[i][0])
                    tags.append(i)
                    n = n-1
                elif records[i][1] in g1s and records[i][0] in g1b:
                    tags.append(i)
                    n = n-1
        if g2 in g1s:
            return 1
        elif g2 in g1b:
            return -1
        else:return 0
            
    ##无语了，用这个堆栈做都超时了，没办法，参考别人的答案吧  
    ################
    # 出错的原因在于：没有考虑特殊情况：如存在无意义的比较，则records永远不为空，
    # 因此再次压入栈的次数不能超过n，否则是循环压入无意义比较
    ################
    def bystack(self, g1, g2, records, n):
        g1b=[g1]
        g1s=[g1]
        while records and n>0:
            print records
            item = records.pop(0)
            if item[0] in g1s :
                if item[1]==g2:
                    return 1
                g1s.append(item[1])
            elif item[1] in g1b:
                if item[0]==g2:
                    return -1
                g1b.append(item[0])
            elif item[1] in g1s and item[0] in g1b:
                continue
            else:
                records.append(item)
                n=n-1
        return 0

       

myObj = Cmp()
# result = myObj.cmp(2,3,[[1,2],[2,4],[1,3],[4,3]],4)
result = myObj.bystack(2,3,[[1,2],[4,4],[1,3],[4,3]],4)
print result
