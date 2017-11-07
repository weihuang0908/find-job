# -*-encoding=utf-8-*-
"""
# 整数拆分（无序拆分，即1+2和2+1等价）问题

## 找出一个整数n的2的幂数的拆分方法
建模成树的生长，每个节点取值1，2...4，子节点值不能比父节点大，这样保证无序拆分不产生重复路径
路径长度大于n时，路径停止生长；路径长度等于n时，保存到结果当中

## 找出一个整数n的2的幂数的拆分方法数
思路动态规划：考虑上述拆分树，奇数拆分结果为一棵根节点为1的树，偶数拆分结果一般为森林
n为奇数时，已知n-1情况下的森林，空降一个值为1的节点作为森林的根节点，则拆分路径与前一个数的拆分一一对应，dp[n] = dp[n-1]
n为偶数时，已知n-1情况下的根节点为1的树，根节点为2，4，…的树与n/2情况下的森林一一对应（乘2即可）。dp[n] = dp[n-1] + dp[n/2]
"""

"""
来源：深信服
找出一个整数的2的幂数的拆分方法数，要求时间复杂度o(n)
例如 3 = 1 + 1 + 1； 3 = 1 + 2 有两种拆分方法
"""
def get_split_count(n):
    """
    给出具体拆分可能数量
    """
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        if i % 2 == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i/2]
    return dp[n]

def get_split_result(n):
    """
    返回所有具体的拆分方法
    n : int 
    """
    ans = []
    dfs(1, n, [], ans)
    print ans

def dfs(now, remain, path, ans):
    """
    get_split_result调用，自顶向下，向ans里填拆分结果
    now : int
    remain : int
    path :  List[int]
    ans : List[List[int]]
    """
    if remain == 0:
        ans.append(path)
    m = now
    while m <= remain:
        dfs(m, remain - m, path + [m,], ans)
        m *= 2

for i in range(2, 20):
    print i, get_split_count(i)




    
