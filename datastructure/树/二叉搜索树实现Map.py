#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2020/3/25
"""
from datastructure.树.二叉树 import BinTree


class BST(BinTree): 
    """二叉搜索树：左子树都小于根结点，右子树都大于根结点"""
    def __init__(self):
        super().__init__()
        # self._root = None  # BST树的根节点
        # self._size = 0     # BST的规模，BST中节点的数目

    # def length(self):
    #     return self._size
    # 
    # def __len__(self):
    #     return self._size
    # 
    # def __iter__(self):
    #     return self._root.__iter__()
    # 
    # def __str__(self):
    #     return self._root.__str__()

    def put(self, key, value):
        """将一个数据项添加到二叉搜索树中，可用于构造二叉搜索树"""
        if self._root:
            self._put(key, value, self._root)
        else:
            # 初始化根节点，BST规模（节点数）加一
            self._root = BinNode(key, value, parent=self._root)
            self._size += 1

    def _put(self, key, value, current_node):
        """
        往二叉搜索树中添加数据项key-value，策略：把当前结点key和待插入结点key值进行比较，
        决定是更换key对应的value值，还是插入到左子树或右子树。
        1、相等 => 更新key对应的value值
        2、小于 => 插到左子树
        3、大于 => 插到右子树
        :param key:
        :param value:
        :param current_node:
        :return:
        """
        if key == current_node.key:
            current_node.value = value
        elif key < current_node.key:
            if current_node.has_left_child():
                # 有左子树，则递归在左子树中查找
                self._put(key, value, current_node.left_child)
            else:
                # 没有左子树，则插入，然后更新BST节点数
                current_node.left_child = BinNode(key, value, parent=current_node)
                self._size += 1
                # 更新树的高度
                self.update_height_above(current_node.left_child)
        else:
            if current_node.has_right_child():
                # 有右子树，则递归在右子树中查找
                self._put(key, value, current_node.right_child)
            else:
                # 没有右子树，则插入，然后更新BST中节点数
                current_node.right_child = BinNode(key, value, parent=current_node)
                self._size += 1
                # 更新树的高度
                self.update_height_above(current_node.right_child)

    def __setitem__(self, key, value):
        """支持dict类似的[]操作，eg：bst[2] = "red" """
        self.put(key, value)

    def get(self, key):
        """根据key，获取value值"""
        if self._root:
            found_node = self._get(key, self._root)
            if found_node:
                return found_node.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """支持dict []获取值操作，eg：print(bst[2])"""
        self.get(key)

    def __contains__(self, key):
        """支持Map（dict）in关键字操作"""
        if self._get(key, self._root):
            return True
        else:
            return False


class BinNode:
    """定义二叉搜索树中结点的数据结构"""
    def __init__(self, key, value, lc=None, rc=None, parent=None):
        self.key = key            # 结点中数据项的key值
        self.value = value        # 结点中数据项的value值
        self.left_child = lc      # 当前结点的左子树
        self.right_child = rc     # 当前结点的右子树
        self.parent = parent      # 当前结点的父节点

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_data(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


if __name__ == '__main__':
    bst = BST()
    bst[9] = "red"
    bst[4] = "blue"
    bst[40] = "green"
    bst[2] = "yellow"
    bst[6] = "black"
    bst[25] = "white"

    print(bst.get(2))
    bst.put(4, "haha")
    print(bst[4])



