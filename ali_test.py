# -*- coding:utf-8 -*-
'''
思路：
dp[m]是一个矩阵，其中第i行第j列表示从i出发经过m步到达j的最短路径；
递推式：dp[x+y][i][j] = min(dp[x][i][p] + dp[y][p][j])对所有p求最小 
dp_sum()函数实现了根据dp[x]和dp[y]计算dp[x+y]

注意到可以将一个整数分解为：2^x + 2^y + 2^z + ...的形式
比如24 = 2^4 + 2^3， 函数encode()完成了相关功能
所以dp[25] = dp_sum(dp[2^4], dp[2^3])
换言之只需要计算dp[2^n]即可,这样时间复杂度就是o(logm n^3)
'''

def encode(num):
    xx = list(str(bin(num)[2:]))
    cnt = len(xx) - 1
    for val in xx:
        if val== '1':
            tmp.append(cnt)
        cnt -= 1
    return tmp

def dp_sum(dp_x, dp_y):  
    dp_m = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            dp_m[i][j] = min([dp_x[i][p] + dp_y[p][j] for p in range(n)])
    return dp_m

def func(n,M,map):
    # dp[M][i][j]表示经过M步从i到达j
    dp = []
    ele_list = encode(M)
    for _ in range(M+1):
        xx = [[0]*n for i in range(n)]
        dp.append(xx)
   
    # dp[1][i][i]不可能到达，设为充分大的数
    for i in range(n):
        dp[1][i][i] = 999999999
   
    # dp[1][i][j] i!=j 就是map[i][j]
    for i in range(n):
        for j in range(n):
            if i != j:
                dp[1][i][j] = map[i][j]
                
    # 计算dp[2^0], dp[2^1],……
    m = 0
    while m < ele_list[0]:
        dp[2**(m+1)] = dp_sum(dp[2**m],dp[2**m])
        m += 1
        
    # 调用dp_sum()计算，比如dp[25] = dp_sum(dp[2^4], dp[2^3])
    dp[M] = dp[2**ele_list[0]]
    ele_list.pop(0)
    while len(ele_list) > 0:
        dp[M] = dp_sum(dp[M], dp[2**ele_list[0]])
        ele_list.pop(0)
    return dp[M]

if __name__=='__main__':
    # 输入数据
    n = int(raw_input())
    m = int(raw_input())
    u = raw_input()
    map = []
    for i in range(n):
        line = [int(x) for x in raw_input().split()]
        map.append(list(line))
    # 输出数据
    res = func(n,m,map)
    print res