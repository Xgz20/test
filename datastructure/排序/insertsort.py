#! /usr/bin/env python
# -*- coding: utf-8 -*-


def insert_sort(alist):
    """
    插入排序，时间复杂度为O(n^2)，从前往后遍历，从1开始
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):
        current_value = alist[i]
        position = i
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value


if __name__ == '__main__':
    test_list = [13, 5, 25, 9, 2, 11]
    insert_sort(test_list)
    print(test_list)
