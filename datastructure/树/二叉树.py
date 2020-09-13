#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2019/12/16
"""
from datastructure.线性表.queue.queue import Queue
from datastructure.线性表.stack.stack import Stack


class BinNode:
    """二叉树节点类"""
    def __init__(self, data, parent=None, left_child=None, right_child=None):
        self.data = data                   # 节点的数据项值
        self.parent = parent               # 节点的父节点
        self.left_child = left_child       # 节点的左子树根节点
        self.right_child = right_child     # 节点的右子树根节点
        self.height = 0                    # 节点的高度
        self.npl = None                    # 左式堆用到
        self.color = None                  # 红黑树用到

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def size(self) -> int:
        """节点的规模（以这个节点为根的子树共有多少个节点）"""
        count = 1
        if self.has_left_child():
            count += self.left_child.size()
        if self.has_right_child():
            count += self.right_child.size()
        return count

    def has_parent(self):
        return self.parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def has_any_child(self):
        return self.left_child or self.right_child

    def insert_as_lc(self, data):
        """将data数据项作为当前节点的左子树插入"""
        self.left_child = BinNode(data, self)
        return self.left_child

    def insert_as_rc(self, data):
        """将data数据项作为当前节点的右子树插入"""
        self.right_child = BinNode(data, self)
        return self.right_child

    def get_successor(self):
        """获取当前节点中序遍历的直接后继节点"""
        if self.has_right_child():
            succ_node = self.right_child
            while succ_node.left_child:
                succ_node = succ_node.left_child
            return succ_node
        else:
            return None


class BinTree:
    """二叉树"""
    def __init__(self):
        self._size = 0
        self._root = None

    def size(self) -> int:
        """获取这个棵树一共有多少个节点"""
        return self._size

    def get_root(self) -> BinNode:
        """获取这棵树的根节点"""
        return self._root

    def set_root(self, bin_node: BinNode):
        self._root = bin_node

    def is_empty(self):
        """判断这棵树是否是空树"""
        return not self._root

    def update_height(self, bin_node: BinNode) -> int:
        """
        更新树中任意节点bin_node的高度，思想：借助左右子树，一个树的高度为左右子树的高度最大值加上1
        Note：单个节点高度为0，空树高度为-1
        :param bin_node: BinNode
        :return: NA
            """

        def stature(node: BinNode) -> int:
            """获取单个节点的高度，考虑空树和单个节点的情况"""
            return node.height if node else -1
        bin_node.height = 1 + max(stature(bin_node.left_child), stature(bin_node.right_child))
        return bin_node.height

    def update_height_above(self, bin_node: BinNode):
        """
        更新树中任意节点bin_node及其祖先的高度,
        算法时间复杂度：O(n=depth(bin_node))，即为bin_node节点的深度
        :param bin_node: BinNode
        :return: NA
        """
        while bin_node:
            self.update_height(bin_node)
            bin_node = bin_node.parent

    def insert_as_lc(self, bin_node: BinNode, data) -> BinNode:
        """
        将元素e作为bin_node的左子树插入（假设树中节点bin_node没有左子树）
        :param bin_node: 树中一个没有左子树的节点
        :param data: 待插入的节点数据项值
        :return: 已经插入的节点
        """
        self._size += 1
        bin_node.insert_as_lc(data)
        self.update_height_above(bin_node)
        return bin_node.left_child

    def insert_as_rc(self, bin_node: BinNode, data) -> BinNode:
        """
        将元素e作为bin_node的右子树插入（假设树中节点bin_node没有右子树）
        :param bin_node: 树中一个没有右子树的节点
        :param data: 待插入的节点数据项值
        :return: 已经插入的节点
        """
        self._size += 1
        bin_node.insert_as_rc(data)
        self.update_height_above(bin_node)
        return bin_node.right_child



"""
遍历二叉树
1、先序遍历
2、中序遍历
3、后序遍历
4、层序遍历
"""


"""######################先序遍历############################"""

"""递归先序遍历二叉树"""
def pre_order_traverse(root: BinNode):
    """递归先序遍历二叉树"""
    if not root:
        return
    # 访问根节点，这里以print()函数打印出来表示访问
    print(root.get_data())
    if root.has_left_child():
        pre_order_traverse(root.left_child)
    if root.has_right_child():
        pre_order_traverse(root.right_child)
"""
算法分析：
上面递归形式的先序遍历二叉树，
时间复杂度：T(n)=O(1)+T(a)+T(n-a-1)=O(n)，
空间复杂度：虽然递归形式没有使用辅助栈，但递归的实现本身就是基于栈的，空间复杂度我们理解为O(h)，h为树的高度
渐进的线性，而递归的特性，在递归栈中每一帧并不能做到足够小，相当于n前面的常系数比较大，
所以需要改进这个算法，让递归形式转化为迭代形式。
"""


def pre_order_traverse_iter(root: BinNode):
    """迭代方式先序遍历二叉树（非递归），根据尾递归借助栈来实现"""
    stack = Stack()  # 辅助栈
    # 树根节点入栈
    if root:
        stack.push(root)
    while not stack.is_empty():  # 在栈变空之前反复循环
        # 弹出并访问当前节点
        root = stack.pop()  # 特别注意节点root的切换
        print(root.get_data())
        # 这里要注意由于栈的后进先出特性，对于先序遍历，右子树要先进栈，左子树后进栈
        if root.has_right_child():
            # 有右子树就入栈，右子树先入后出
            stack.push(root.right_child)
        if root.has_left_child():
            # 有左子树就入栈，左子树后入先出
            stack.push(root.left_child)
"""
算法分析：
上面这种根据尾递归转化而来的迭代先序遍历算法，时间复杂度为O(n),空间复杂度为O(h),h为树的高度。
但上面这种迭代方式不适用于二叉树的中序遍历和后序遍历，所以我们还要对迭代方式进行改进。
"""


def pre_order_traverse_iter2(root: BinNode):
    """非递归的先序遍历二叉树升级版，利用分摊思想"""
    stack = Stack()  # 辅助栈，栈中存放的都是右子树节点
    while True:  # 以右子树为单位，逐批访问节点
        # 访问子树root的左侧链，右子树入栈缓冲
        visit_along_left_branch(root, stack)
        if stack.is_empty():  # 栈空即退出
            break
        root = stack.pop()  # 弹出下一子树的根，相当于切换到下个右子树上


def visit_along_left_branch(root: BinNode, stack: Stack):
    while root:
        print(root.get_data())  # 访问当前节点
        # 右子树入栈（将来逆序出栈），注意这里没有判断右子树是否为None
        stack.push(root.right_child)
        root = root.left_child  # 沿左侧链下行
        # 这里思考，上面程序，右子树入栈前没有加判空处理，则可能就会有None值入栈，这里有没有必要加判空？
        # 答：其实这里没有必要加判空，因为如果右子树为空，直接空值入栈，
        #    则在出栈后进入visit_along_left_branch()函数，也会在while循环的地方被拦截下来。当然也可以加判空。

"""
算法分析：
时间复杂度为O(n)[#pop = #push = #print = O(n) = 分摊O(1)]
空间复杂度为O(h)，h为树的高度
"""




"""######################中序遍历############################"""


"""递归中序遍历二叉树"""
def in_order_traverse(root: BinNode):
    """递归中序遍历二叉树"""
    if not root:
        return
    if root.has_left_child():
        in_order_traverse(root.left_child)
    print(root.get_data())
    if root.has_right_child():
        in_order_traverse(root.right_child)


"""迭代中序遍历二叉树"""
def in_order_traverse_iter(root: BinNode):
    """迭代形式中序遍历二叉树"""
    stack = Stack()  # 辅助栈（栈中存放的是左侧链节点：包括根节点和右子树）
    while True:  # 反复地
        go_along_left_branch(root, stack)  # 从当前节点出发，逐批入栈
        if stack.is_empty():  # 直至所有节点处理完毕
            break
        root = stack.pop()  # root的左子树或为空，或已遍历（等效于空）
        print(root.get_data())  # 立即访问之
        root = root.right_child  # 再转向右子树（可能为空，留意处理手法）


def go_along_left_branch(root: BinNode, stack: Stack):
    """延着左侧链，左子树根依次入栈（其实栈中存放的是根节点和左子树根节点，这里都当成左侧链上节点处理）"""
    while root:
        stack.push(root)
        root = root.left_child  # 反复的入栈，沿左分支深入

"""
算法分析：
go_along_left_branch()方法每个元素只会入栈一次，while循环会遍历n次，
整个算法的时间复杂度为O(n),并且这个n的常系数相对于递归遍历算法来说是比较小的。
空间复杂度：由于使用了辅助栈，空间复杂度为O(h)，h为树的深度。
"""




"""######################后序遍历############################"""

"""递归形式后序遍历二叉树"""
def post_order_traverse(root: BinNode):
    """递归形式后序遍历二叉树"""
    if not root:
        return
    if root.has_left_child():
        post_order_traverse(root.left_child)
    if root.has_right_child():
        post_order_traverse(root.right_child)
    # 访问根节点
    print(root.get_data())


"""迭代形式后序遍历二叉树：两个栈"""
def post_order_traverse_with_two_stack(root: BinNode):
    """迭代形式后序遍历二叉树，使用两个栈"""
    if not root:
        return
    stack1 = Stack()  # 转换栈，用于调整节点入stack2栈的顺序
    stack2 = Stack()  # 存放后序序列的栈
    stack1.push(root)
    while not stack1.is_empty():  # 循环遍历栈1中的节点，直至栈1为空
        # 栈1中的节点出栈
        node = stack1.pop()
        # 节点进入栈2
        if node:
            stack2.push(node)
            # 检查当前节点的左右子树，注意入栈1次序是先左后右
            if node.has_left_child():
                # 节点的左子树入栈1
                stack1.push(node.left_child)
            if node.has_right_child():
                # 当前节点的右子树入栈1
                stack1.push(node.right_child)
    while not stack2.is_empty():  # 将栈2中的元素全部出栈
        ele = stack2.pop()
        # 立即访问
        print(ele.get_data())



"""迭代形式后序遍历二叉树：一个栈"""
"""
使用一个栈，迭代形式后序遍历二叉树，技巧是设置一个指针指向上个出栈的节点
算法思想：
用current_node表示栈顶元素，last_node表示最近出栈的元素，初始化为根节点
1、申请一个栈将根节点root压入栈，初始化last_node指向根节点
2、如果栈不为空，则current_node赋值为栈顶元素
---2.1 如果current_node的左孩子不为空，并且last_node不等于current_node的左孩子，也不等于current_node的右孩子，
       那么就将current_node的左孩子压入栈。（如果last_node等于当前节点的左孩子，就说明左子树已经访问过了，
       否则就代表还没有打印过，就应该将左孩子或者右孩子入栈）
---2.2 在2.1条件不成立的条件下，如果current_node的右孩子不为空，并且不等于last_node，就说明右子树还没有处理过，
       这个时候就应该将current_node的右孩子压入栈。
---2.3 如果前两个条件都不成立，就说明current_node的左子树和右子树已经访问完毕了，或者当前节点为叶子节点，
       此时就应该将栈顶元素出栈，并且令last_node重新指向这个出栈的元素。
3. 一直重复步骤2直到栈为空，结束程序
"""
def post_order_traverse_with_one_stack(root: BinNode):
    """迭代形式后序遍历二叉树，使用标记指针方式，使用一个栈"""
    if not root:
        return
    stack = Stack()
    stack.push(root)
    last_node = root  # 除了第一次指向根节点，后面都指向出栈的节点，每次出栈后就更新这个指针的值
    while not stack.is_empty():
        current_node = stack.peek()
        if current_node.left_child is not None and current_node.left_child != last_node \
                and current_node.right_child != last_node:
            stack.push(current_node.left_child)
        elif current_node.right_child is not None and current_node.right_child != last_node:
            stack.push(current_node.right_child)
        else:
            stack.pop()
            last_node = current_node
            print(current_node.get_data())


"""######################层序遍历############################"""

"""
层序遍历
算法思想：借助一个队列，每个元素在访问之后，就将其左子树、右子树入队。
"""
def level_order_traverse(root: BinNode):
    """迭代形式的层序遍历二叉树，使用队列"""
    quequ = Queue()  # 辅助队列
    # 根节点入队
    quequ.enqueue(root)
    while not quequ.is_empty():
        ele = quequ.dequeue()
        print(ele.get_data())
        if ele.has_left_child():
            quequ.enqueue(ele.left_child)
        if ele.has_right_child():
            quequ.enqueue(ele.right_child)

"""
算法分析：
迭代形式的层序遍历二叉树，时间复杂度为O(n)，由于使用了一个队列，空间复杂度为O(w)，w为树的宽度
"""



if __name__ == '__main__':
    tree = BinTree()
    root = BinNode("A")
    tree.set_root(root)
    b_node = tree.insert_as_lc(root, "B")
    c_node = tree.insert_as_rc(root, "C")
    d_node = tree.insert_as_lc(b_node, "D")
    e_node = tree.insert_as_rc(b_node, "E")
    f_node = tree.insert_as_rc(c_node, "F")
    g_node = tree.insert_as_lc(e_node, "G")

    pre_order_traverse(tree.get_root())
    in_order_traverse_iter(tree.get_root())
    post_order_traverse_with_one_stack(tree.get_root())
    level_order_traverse(tree.get_root())



