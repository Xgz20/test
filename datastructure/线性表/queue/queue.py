#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2019/12/15
"""


class Queue(object):
    """
    队列（顺序表实现的队列）
    """
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """
        入队操作，内部列表索引为0的元素作为队尾，时间复杂度为O(n)
        :param item:
        :return:
        """
        self.__list.insert(0, item)

    def dequeue(self):
        """
        出队操作，内部列表最后一个元素作为队首，时间复杂度为O(1)
        :return:
        """
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def __str__(self):
        return self.__list.__str__()


class TwoQueStack:
    def __init__(self):
        self.a_queue = Queue()
        self.b_queue = Queue()

    def push(self, value):
        """
        进栈
        :param value:
        :return:
        """
        if not self.a_queue.is_empty():
            self.a_queue.enqueue(value)
        elif not self.b_queue.is_empty():
            self.b_queue.enqueue(value)
        else:
            self.a_queue.enqueue(value)

    def pop(self):
        """
        出栈
        :return:
        """
        if self.a_queue.is_empty() and self.b_queue.is_empty():
            return
        if not self.a_queue.is_empty():
            for _ in range(self.a_queue.size() - 1):
                self.b_queue.enqueue(self.a_queue.dequeue())
            return self.a_queue.dequeue()
        elif not self.b_queue.is_empty():
            for _ in range(self.b_queue.size() - 1):
                self.a_queue.enqueue(self.b_queue.dequeue())
            return self.b_queue.dequeue()
        else:
            raise ValueError

    def is_empty(self):
        return self.a_queue.is_empty() and self.b_queue.is_empty()

    def size(self):
        return self.b_queue.size() if self.a_queue.is_empty() else self.a_queue.size()

    def __str__(self):
        pass


if __name__ == '__main__':
    # queue = Queue()
    # print("is_empty：", queue.is_empty())
    # queue.enqueue("abc")
    # queue.enqueue(False)
    # queue.enqueue(15)
    # print("is_empty：%s, size：%s" % (queue.is_empty(), queue.size()))
    # print("dequeue：", queue.dequeue())
    stack = TwoQueStack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

