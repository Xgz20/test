#! /usr/bin/env python
# -*- coding: utf-8 -*-


def patition(alist, low, high):
    """
    一次划分
    :param alist:
    :param low:
    :param high:
    :return:
    """
    # 用子表的第一个记录作为枢轴
    pivot_value = alist[low]
    while low < high:
        # 从右端找第一个比枢轴小的数据
        while low < high and pivot_value <= alist[high]:
            high = high - 1
        alist[low] = alist[high]  # 将小于枢轴的记录移到左边
        # 从左端找第一个比枢轴大的数据
        while low < high and alist[low] <= pivot_value:
            low = low + 1
        alist[high] = alist[low]  # 将大于枢轴的记录移到右边
    # 当low等于high时结束循环，并将枢轴移到“中间”
    alist[low] = pivot_value
    # 返回枢轴所在位置
    return low


def qsort(alist, low, high):
    """
    递归方法，不断调用划分方法，直至low==high
    :param alist:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        # 找到枢轴位置
        pivot_position = patition(alist, low, high)
        # 对枢轴左半部分进行快速排序
        qsort(alist, low, pivot_position - 1)
        # 对枢轴右半部份进行快速排序
        qsort(alist, pivot_position + 1, high)


def quick_sort(alist):
    if alist is None or len(alist) < 2:
        return alist
    qsort(alist, 0, len(alist) - 1)


"""
第二种快速排序算法
"""
def quick_sort2(alist):
    """
    利用python语言的特性简化快速排序算法
    :param alist:
    :return:
    """
    if len(alist) < 2:
        return alist
    else:
        pivot_value = alist[0]
        less = [item for item in alist[1:] if item <= pivot_value]
        greater = [item for item in alist[1:] if item > pivot_value]
        return quick_sort2(less) + [pivot_value] + quick_sort2(greater)


if __name__ == '__main__':
    test_list = [13, 5, 25, 9, 2, 11]
    # quick_sort(test_list)
    # print(test_list)

    print(quick_sort2(test_list))
