# -*-encoding=utf-8-*-
"""
全面复习各种奇怪的排序
"""

"""
直接插入排序
"""
def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp
    return nums

"""
归并排序
"""
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        mid = len(nums) / 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)

def merge(nums1, nums2):
    i = 0
    j = 0
    len1 = len(nums1)
    len2 = len(nums2)
    ans = []
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1
    if i == len1:
        ans.extend(nums2[j:])
    else:
        ans.extend(nums1[i:])
    return ans

"""
堆排序
"""
def heap_sort(nums):
    build_heap(nums)
    length = len(nums)
    for i in range(1, length+1):
        nums[0], nums[length - i] = nums[length - i], nums[0]
        adjust(nums, 0, length - i)
    return nums

def build_heap(nums):
    length = len(nums)
    for i in range(length/2, -1, -1):
        adjust(nums, i, length)

def adjust(nums, i, l):
    """
    最大堆
    """
    max_idx = i
    if 2 * i + 2 < l:
        if nums[2 * i + 2] > nums[max_idx]:
            max_idx = 2 * i + 2
    if 2 * i + 1 < l:
        if nums[2 * i + 1] > nums[max_idx]:
            max_idx = 2 * i + 1
    if max_idx != i:
        nums[i], nums[max_idx] = nums[max_idx], nums[i]
        adjust(nums, max_idx, l)

"""
快排
"""
def quick_sort(nums):
    helper(nums, 0, len(nums) - 1)
    return nums

def helper(nums, start, end):
    if start < end:
        p = divide(nums, start, end)    
        helper(nums, start, p-1)
        helper(nums, p+1, end)

def divide(nums, start, end):
    """
    nums[j] 是有序区的最后一个比pivot小的数
    nums[j+1] 是有序区的第一个比pivot大的数
    """
    pivot = nums[end]
    j = start - 1
    for i in range(start, end):
        if nums[i] < pivot:
            nums[j+1], nums[i] = nums[i], nums[j+1]
            j += 1
    nums[end] = nums[j+1]
    nums[j+1] = pivot
    return j+1


print insert_sort([4,9,3,2,5,6,8,7,1])
print merge_sort([4,9,3,2,5,6,8,7,1])
print heap_sort([4,9,3,2,5,6,8,7,1])
print quick_sort([4,9,3,2,5,6,8,7,1])
