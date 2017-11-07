# -*-encoding=utf-8-*-
"""
用单调栈解数组元素边界问题
给一个数组，返回一个大小相同的数组。返回的数组的第i个位置的值应当是，对于原数组中的第i个元素，至少往右走多少步，才能遇到一个比自己大的元素（如果之后没有比自己大的元素，或者已经是最后一个元素，则在返回数组的对应位置放上-1）
e.g. [5,3,1,2,4]
输出 [-1,3,1,1,-1]
对于第0个数字5，之后没有比它更大的数字，因此是-1，对于第1个数字3，需要走3步才能达到4
"""
def nextExceed(nums):
    """
    用单调栈求右边第一个比我大的数和我的距离
    stack中的元素永远是单调递增的，保存元素的索引
    """
    if len(nums) == 0:
        return []
    ans = [-1 for i in nums]
    stack = [len(nums)-1, ]
    for i in range(len(nums)-2, -1, -1):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans

print nextExceed([5,3,1,2,4])




"""
给定一段数组，求每个区间的最小值乘这段区间的和，输出每个区间得到的最大值。
e.g. [1, 2, 6]
输出 6 * 6 = 36
"""
def solve(nums):
    """
    nums有n个元素，则分为n种情况，即以当前元素为最小值的区间*当前元素的值
    """
    dp_sum = [0 for i in range(len(nums))]
    for i, n in enumerate(nums):
        if i == 0:
            dp_sum[i] = n
        else:
            dp_sum[i] = dp_sum[i-1] + n
    length = len(nums)
    left_bound = [i for i in range(length)]
    right_bound = [i for i in range(length)]
    # 从左向右扫描，找出每个元素的左界
    stack = [0]
    for i in range(1, length-1):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            stack.pop()
        if len(stack)!=0:
            left_bound[i] = stack[-1]
        stack.append(i)
    # 从右向左扫描，找出每个元素的右界
    stack = [length-1]
    for i in range(length-2,-1,-1):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            stack.pop()
        if len(stack)!=0:
            right_bound[i] = stack[-1]
        stack.append(i)
    # 求结果
    ans = [(dp_sum[right_bound[i]] - dp_sum[left_bound[i]] + nums[left_bound[i]]) * nums[i] \
            for i in range(length)]
    return max(ans)

print solve([1,2,6]) 



