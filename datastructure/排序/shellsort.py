#! /usr/bin/env python
# -*- coding: utf-8 -*-


def group_sort(alist, start_positon, gap):
    """
    对每个分组排序
    :param alist:
    :param start_positon:
    :param gap:
    :return:
    """
    for i in range(start_positon + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        # 特别注意等于间隔也可以
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value


def shell_sort(alist):
    """
    希尔排序，时间复杂度为O(n^(3/2))，介于O(n)和O(n^2)之间,
    算法思想是先分组，然后对分组数据进行插入排序
    :param alist:
    :return:
    """
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            group_sort(alist, i, gap)
        gap = gap // 2


if __name__ == '__main__':
    test_list = [13, 5, 25, 9, 2, 11]
    shell_sort(test_list)
    print(test_list)