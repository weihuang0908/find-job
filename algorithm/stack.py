# -*-encoding=utf-8-*-

"""
假设入栈序列是1,2..n
检查一个出栈序列是否合法

思路：判断出栈序列的每个数的右边的比该数的小的数组成的子序列是否递减
例如：入栈顺序123，出栈顺序312不合法
1，2如果比3先出栈，则顺序可以随意，若比3后出栈，一定是递减序列
"""
def check_stack_out(seq):
    length = len(seq)
    for i in range(length):
        key = seq[i]
        last = seq[i]
        for j in range(i+1, length):
            if seq[j] < key:
                if seq[j] > last:
                    return False
                else:
                    last = seq[j]
    return True

def test_check_stack_out():
    items = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    ans = [True, True, True, True, False, True]
    for q, a in zip(items, ans):
        print q, a
        assert(check_stack_out(q) == a)

test_check_stack_out()


"""
所有出栈可能计数

思路：卡特兰数c(2n, n)/(n+1)
h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)*h(0) (n>=2)
h(3)=h(0)*h(2)+h(1)*h(1)+h(2)*h(0)=1*2+1*1+2*1=5
"""
def count_all_stack_out(n):
    """
    n: int
    """
    dp = {}
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = 0
        for j in range(1, i+1):
            dp[i] += dp[i-j] * dp[j-1] 
    print dp[n]

"""
来源：深信服
打印所有出栈顺序
"""
def print_all_stack_out(n):
    """
    n: int
    """
    print helper(1, n)


def helper(left, right):
    """
    入栈顺序123，分别考虑某个元素k(k=1,2,3)最后出栈的情况，
    则出栈顺序有3种情况，前k-1个元素和后n-k个元素的顺序是独立的
    即 两重循环 ans = left_seq + right_Seq + [k,]
    left: int
    right: int
    """
    if left > right:
        return [[]]
    if left == right:
        return [[left,]]
    ans = []
    for i in range(left, right+1):
        tmp_left = helper(left, i-1)
        tmp_right = helper(i+1, right)
        for item_l in tmp_left:
            for item_r in tmp_right:
                ans.append(item_l + item_r + [i,])
    return ans

print_all_stack_out(3)        
count_all_stack_out(3)        

"""
拓展1:
leetcode 241 算术表达式不同加括号方式的结果
e.g. “2-1-1” => ((2-1)-1)=0, （2-(1-1)=2）=> [0 , 2]
以第k个运算符为轴，前面子式的M种结果和后面子式的N种结果是独立的，当前子式的结果为二重循环的m op n
"""
def diff_para_ways(op_str):
    ans = []
    for i, c in enumerate(op_str):
        if c in ['+','-','*']:
            tmp_l = diff_para_ways(op_str[:i])
            tmp_r = diff_para_ways(op_str[i+1:])
            for m in tmp_l:
                for n in tmp_r:
                    if c == '+':
                        ans.append(m+n)
                    if c == '-':
                        ans.append(m-n)
                    if c == '*':
                        ans.append(m*n)
    if len(ans)==0:
        ans.append(int(op_str))
    return ans
assert(set(diff_para_ways("2-1-1"))==set([2,0]))



"""
拓展2：
12个高矮不同的人，排成两排，每排必须是从矮到高排列，而且第二排比对应的第一排的人高，问排列方式有多少种？
问题分析（http://blog.csdn.net/hackbuteer1/article/details/7450250）:
    我们先把这12个人从低到高排列,然后,选择6个人排在第一排,那么剩下的6个肯定是在第二排.
    用0表示对应的人在第一排,用1表示对应的人在第二排,那么含有6个0,6个1的序列,就对应一种方案.
    比如000000111111就对应着
    第一排：0 1 2 3 4 5
    第二排：6 7 8 9 10 11
    问题转换为，这样的满足条件的01序列有多少个。
    也就是要求，在每个’1’的前面，’0’的个数大于’1’的个数。
    如果把0看成入栈操作，1看成出栈操作，就是说给定6个元素，合法的入栈出栈序列有多少个。
"""
