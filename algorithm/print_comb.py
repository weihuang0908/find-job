# -*-encoding=utf8-*-
"""
给定m, n
打印从n个数里取m个的所有组合
"""
def print_comb(m, n):
    ans = []
    helper(0, m, n, [], ans)
    print ans

def helper(now, remain, n, path, ans):
    """
    考虑树的生长，子节点的now应大于父节点的now, 向下生长的深度限制为remain
    """
    if remain == 0:
        ans.append([i for i in path])
    for i in range(now+1, n+1):
        path.append(i)
        helper(i, remain-1, n, path, ans)
        path.pop()

print_comb(2, 5)

"""
给定m, n
打印从n个数里取m个的排列
"""
def print_perm(m, n):
    ans = []
    helper_perm([i for i in range(1, n+1)], m, [], ans)
    print ans

def helper_perm(remain, remain_depth, path, ans):
    """
    同样考虑树的生长，子节点的候选集为父节点候选集与父节点的差集，向下生长的深度限制为remain_depth
    """
    if remain_depth == 0:
        ans.append([c for c in path])
    for now in remain:
        path.append(now)
        helper_perm([c for c in remain if c!=now], remain_depth-1, path, ans)
        path.pop()

print_perm(2, 3)

"""
给定n
打印n个数的全排列
"""
def print_perm_all(n):
    ans = helper_perm_all([i for i in range(1, n+1)], 0)
    print ans

def helper_perm_all(nums, idx):
    """
    递归，假设知道如何求后面n-1个数的全排列，
    可以依次将第1个数与第i个数交换，去求后n-1个数的全排列，再在每个求得的子排列头插一第1个数即可
    e.g. 已知如何求2个数的全排列, 现在要求3个数的全排列
    1 2 3 = > [1] + [2,3] , [1] + [3,2]
    2 1 3 = > [2] + [1,3] , [2] + [3,1]
    3 2 1 = > [3] + [2,1] , [3] + [1,2]
    """
    if idx == len(nums):
        return [[]]
    ans = []
    for i in range(idx, len(nums)):
        nums[i], nums[0] = nums[0], nums[i]
        tmp = helper_perm_all(nums, idx+1)
        for item in tmp:
            ans.append([nums[0], ] + item)
        nums[i], nums[0] = nums[0], nums[i]
    return ans
print_perm_all(3)






