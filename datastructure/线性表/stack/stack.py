#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2019/12/15
"""


class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """
        入栈操作，时间复杂度为O(1)
        :param item: 入栈的元素
        :return: 无返回值
        """
        self.__list.append(item)

    def pop(self):
        """
        出栈操作，返回栈顶元素，并将栈顶元素从栈中删除，
        时间复杂度为O(1)
        :return: 返回栈顶元素
        """
        return self.__list.pop()

    def peek(self):
        """
        出栈操作，返回栈顶元素，不会将栈顶元素从栈中删除，
        时间复杂度为O(1)
        :return: 返回栈顶元素
        """
        return self.__list[len(self.__list) - 1]

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def __str__(self):
        return self.__list.__str__()


class TwoStackQueue:
    def __init__(self):
        # a栈用于存放入队元素
        self.a_stack = Stack()
        # b栈用于元素出队
        self.b_stack = Stack()

    def enqueue(self, item):
        self.a_stack.push(item)

    def dequeue(self):
        if self.b_stack.is_empty():
            if self.a_stack.is_empty():
                return None
            else:
                # 将A栈中的所有元素出栈并移到B栈中
                while not self.a_stack.is_empty():
                    self.b_stack.push(self.a_stack.pop())
                return self.b_stack.pop()
        else:
            return self.b_stack.pop()

    def is_empty(self):
        return self.a_stack.is_empty() and self.b_stack.is_empty()

    def size(self):
        return self.a_stack.size() + self.b_stack.size()

    def __str__(self):
        """
        待实现
        :return:
        """
        # result = []
        # temp = self.copy()
        # while not self.is_empty():
        #     result.append(temp.dequeue())
        pass


if __name__ == '__main__':
    # stack = Stack()
    # print("is_empty：", stack.is_empty())
    # stack.push("abc")
    # print("is_empty：%s, size：%s" % (stack.is_empty(), stack.size()))
    # stack.push(True)
    # stack.push(15)
    # print(stack)
    # print("pop：", stack.pop())
    # print("peek：", stack.peek())

    two_stack_queue = TwoStackQueue()
    print("操作顺序是入队1,2,3，出队1，入队4，出队2，入队5，出队3，出队4")
    two_stack_queue.enqueue(1)
    two_stack_queue.enqueue(2)
    two_stack_queue.enqueue(3)
    # 当前队列顺序为1,2,3
    print(two_stack_queue.dequeue())
    two_stack_queue.enqueue(4)
    print(two_stack_queue.dequeue())
    two_stack_queue.enqueue(5)
    print(two_stack_queue.dequeue())
    print(two_stack_queue.dequeue())
    print(two_stack_queue.dequeue())




