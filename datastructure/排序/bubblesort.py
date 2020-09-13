#! /usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(alist):
    """
    冒泡排序，时间复杂度为O(n^2)
    :param alist:
    :return:
    """
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def short_bubble_sort(alist):
    """
    短路冒泡排序，思想是如果一趟比较，没有交换则说明列表已有序
    :param alist:
    :return:
    """
    exchange = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                # 有交换才赋值为True，进行下一次遍历
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        pass_num = pass_num - 1


if __name__ == '__main__':
    test_list = [13, 5, 25, 9, 2, 11]
    # bubble_sort(test_list)
    short_bubble_sort(test_list)
    print(test_list)
