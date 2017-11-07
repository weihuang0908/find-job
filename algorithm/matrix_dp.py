# -*-encoding=utf8-*-
"""
给定二维数组matrix
找出和最大子数组，返回最大和
"""
def max_sub_matrix_sum(matrix):
    """
    思路：动态规划，三层循环
    """
    h = len(matrix)
    w = len(matrix[0])
    ans = -100000
    for i in range(h):
        b = [0 for n in range(w)]
        for j in range(i, h):
            for k in range(w):
                b[k] += matrix[j][k]
            last = -10000
            for k in range(w):
                if last > 0:
                    now = b[k] + last
                else:
                    now = b[k]
                if now > ans:
                    ans = now
                last = now
    return ans

a = [[-5,-6,-7],[1,2,-3],[3,4,5]]
print max_sub_matrix_sum(a)





