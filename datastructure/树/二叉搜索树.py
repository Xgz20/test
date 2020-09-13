#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2020/4/12
"""
from datastructure.树.二叉树 import BinTree, BinNode, in_order_traverse


class BST(BinTree):
    """二叉搜索树，继承于二叉树"""
    def __init__(self):
        super().__init__()
        self._hot = None  # 指向命中节点的父节点

    def search(self, key) -> BinNode:
        """查找关键码"""
        return self.search_in(self._root, key, self._hot)

    def search_in(self, current_node: BinNode, key, hot: BinNode) -> BinNode:
        """
        递归形式在树（子树）中查找关键码key
        :param current_node: 当前（子）树根
        :param key: 查找的数据项（关键码）
        :param hot: BinNode 记忆热点，指向命中节点的父节点
        :return: 找不到返回None，若找到返回目标节点
        """
        if not current_node or key == current_node.data:
            return current_node
        hot = current_node  # 记下当前（非空）节点
        if key < current_node.data:
            return self.search_in(current_node.left_child, key, hot)
        else:
            return self.search_in(current_node.right_child, key, hot)
    """
    算法分析：
    时间复杂度：运行时间正比于返回节点的深度，不超过树高O(h)，h为树的高度
    """

    def insert(self, key) -> BinNode:
        target_node = self.search(key)                    # 查找目标，另外初始化self._hot
        if not target_node:                               # 为了禁止雷同元素，故仅在查找失败时（目标节点不存在）才实施插入操作
            target_node = BinNode(key, parent=self._hot)  # 在target_node处创建新节点，以_hot为父节点
            self._size += 1                               # 更新树的规模
            self.update_height_above(target_node)         # 更新target_node及其历代祖先的高度
        return target_node                                # 无论待插入的key是否在原树中，至此总有node.data == key
    """
    算法分析：
    时间复杂度：search操作和更新树高操作，两者时间和也不会超过 O(h)，h为树的高度，
              或者表示为O(log(n))，n为元素个数。
    验证：对于首个节点插入之类的边界情况，均可正确处置。
    """

    def remove(self, key) -> bool:
        """删除指定关键码对应的节点，删除成功返回True，否则返回False"""
        target_node = self.search(key)          # 定位目标节点，并初始化self._hot
        if not target_node:
            return False                        # 目标节点不存在，直接返回False
        self.remove_at(target_node, self._hot)  # 分两大类情况实施删除
        self._size -= 1                         # 更新全树的规模
        self.update_height_above(self._hot)     # 更新_hot节点及其历代祖先的高度
        return True                             # 返回成功与否，由返回值指示，True:删除成功，False：删除失败

    def remove_at(self, target_node: BinNode, hot: BinNode) -> BinNode:
        """
        删除目标节点target_node，返回目标节点的接替者
        :param target_node: 目标节点
        :param hot: 目标节点的父节点
        :return: 目标节点的接替者
        """
        temp_node = target_node
        # successor_node = None  # 实际被删除节点的接替者
        if not target_node.has_left_child():
            successor_node = target_node.right_child  # 没有左子树，右子树根节点接替
        elif not target_node.has_right_child():
            successor_node = target_node.left_child   # 没有右子树，左子树根节点接替
        else:
            # 待删除节点，左、右子树都存在，此时去找删除节点的直接后继节点
            temp_node = temp_node.get_successor()
            # 将目标节点的直接后继节点的数据复制到目标节点，这样最终把后继结点删掉即可。
            # 注意这种“移花接木”策略
            target_node.data, temp_node.data = temp_node.data, target_node.data
            u = temp_node.parent
            if u is target_node:
                # 待删除节点是目标节点的右子树的根
                u.right_child = temp_node.right_child
                successor_node = temp_node.rigth_child
            else:
                # 待删除节点不是目标节点的右子树的根
                u.left_child = temp_node.right_child
                successor_node = temp_node.right_child
            self.update_height_above(u)
            self._hot = u  # 更新self._hot
        hot = temp_node.parent
        if successor_node:
            successor_node.parent = hot
        # release(temp_node.data)  # C/C++需要释放删除节点对象及其里面的数据项，Java、Python不需要
        # release(temp_node)
        return successor_node  # 返回接替者
    """
    算法分析：
    时间复杂度：O(h)，h为树的高度
    """


if __name__ == '__main__':
    bst = BST()
    root = bst.insert(9)
    bst.set_root(root)
    bst.insert(4)
    bst.insert(40)
    bst.insert(2)
    bst.insert(6)
    bst.insert(25)
    bst.insert(50)
    bst.insert(30)

    in_order_traverse(bst.get_root())
