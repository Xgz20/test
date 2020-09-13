#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2020/3/24
"""


class BinHeap:
    """二叉堆（此处构造小根堆）"""
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, ele):
        """
        往小根堆中插入一个数据项ele
        :param ele: 待插入数据项
        :return:
        """
        self.heap_list.append(ele)
        self.current_size = self.current_size + 1
        # 调整小根堆
        self.ele_up(ele, self.current_size)

    def ele_up(self, ele, index):
        """
        元素上浮操作，使小根堆成立
        :param ele:
        :param index:
        :return:
        """
        while index // 2 > 0:
            if self.heap_list[index // 2] < ele:
                self.heap_list[index // 2], ele = ele, self.heap_list[index // 2]
            index = index // 2

    def del_min(self):
        """
        返回小根堆的根（最小的元素），并将其从小根堆中移除
        算法思想：用最后一个元素替代最小元素，然后使用“下沉”操作使树保持小根堆特性
        :return:
        """
        if self.current_size == 0:
            return -1
        # 保存待删除的结点，以便后面返回
        result = self.heap_list[1]
        # 用最后一个值替换要删除的结点
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.ele_down(1)
        return result

    def ele_down(self, index):
        """
        元素下沉操作
        算法思想：根据根结点index，找到这个结点该下沉到左子树还是右子树上，判断条件是
        谁小就下沉到谁
        :param index: 树或子树根结点的位置，动态改变的
        :return:
        """
        while 2 * index <= self.current_size:
            min_index = self.find_min_index(index)
            if self.heap_list[index] > self.heap_list[min_index]:
                self.heap_list[index], self.heap_list[min_index] = \
                    self.heap_list[min_index], self.heap_list[index]
            index = min_index

    def find_min_index(self, index):
        """
        找到待下沉的结点需要往哪边下沉，策略是哪边小就往哪边下沉；
        另外考虑没有右子树的情况（小根堆是个完全二叉树，所以不用考虑有右子树没有左子树的情况）
        :param index:
        :return:
        """
        # 考虑没有右子树的情况
        if 2 * index + 1 > self.current_size:
            return 2 * index
        if self.heap_list[2 * index] < self.heap_list[2 * index + 1]:
            return 2 * index
        else:
            return 2 * index + 1

    def build_heap(self, input_list):
        """
        使用列表创建一个新的小根堆
        :param input_list:
        :return:
        """
        index = len(input_list) // 2
        self.current_size = len(input_list)
        self.heap_list = [0] + input_list[:]
        while index > 0:
            self.ele_down(index)
            index = index - 1

    def size(self):
        return self.current_size

    def get_heap_list(self):
        return self.heap_list


if __name__ == '__main__':
    new_heap = BinHeap()
    new_heap.build_heap([9, 3, 6, 5, 2])

    print(new_heap.get_heap_list())

    print(new_heap.del_min())
    print(new_heap.del_min())
    print(new_heap.del_min())
    print(new_heap.del_min())
    print(new_heap.del_min())
    print(new_heap.del_min())
