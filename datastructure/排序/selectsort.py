#! /usr/bin/env python
# -*- coding: utf-8 -*-


def select_sort(alist):
    """
    选择排序，时间复杂度O(n^2)，选出最大值的下标，
    然后将这个最大值与最后一个数交换，主要体现在一个“选择”上
    :param alist:
    :return:
    """
    for i in range(len(alist)-1, 0, -1):
        max_position = 0
        for j in range(1, i + 1):
            if alist[j] > alist[max_position]:
                max_position = j
        alist[i], alist[max_position] = alist[max_position], alist[i]


if __name__ == '__main__':
    test_list = [13, 5, 25, 9, 2, 11]
    select_sort(test_list)
    print(test_list)

