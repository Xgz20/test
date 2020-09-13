#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Xgz
@Date: 2020/3/12
"""


"""
使用狄克斯特拉算法求最短路径
注：狄克斯特拉算法仅适用于权重为正的有向图
"""
# 图的结构使用三个字典来表示，另外用一个列表来存储已处理的节点
# graph表用来存储节点与节点的邻居关系
graph = dict()
graph['X'] = {}  # 用X表示起点
graph['X']['A'] = 5
graph['X']['B'] = 2
graph['A'] = {}
graph['A']['C'] = 2
graph['A']['D'] = 4
graph['B'] = {}
graph['B']['A'] = 8
graph['B']['C'] = 7
graph['C'] = {}
graph['C']['Y'] = 1
graph['D'] = {}
graph['D']['C'] = 6
graph['D']['Y'] = 3
graph['Y'] = {}  # 用Y表示终点，终点没有任何邻居
infinity = float("inf")

# costs表用来存储起点到该节点的开销，可以是最短距离或者最短时间等权重。
# 如果从起点无法直达该节点，则用最大值infinity表示。costs表后期会动态更新。
costs = dict()
costs['A'] = 5
costs['B'] = 2
costs['C'] = infinity
costs['D'] = infinity
costs['Y'] = infinity

# parents表用于存储当前节点的父节点，后期会动态更新。
parents = dict()
parents['A'] = 'X'
parents['B'] = 'Y'
parents['C'] = None
parents['D'] = None
parents['Y'] = None


def find_lowest_cost_node(costs_table):
    """
    找到开销最小的节点
    :param costs_table:
    :return:
    """
    low_cost = float("inf")
    low_cost_node = None
    for item in costs_table.keys():
        if item not in processed and low_cost > costs_table[item]:
            low_cost = costs_table[item]
            low_cost_node = item
    return low_cost_node


# 用于存储已处理过的节点
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        # 从起点经过node节点到邻居节点n的开销
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            # 更新当前节点的开销
            costs[n] = new_cost
            # 更新当前节点的父节点
            parents[n] = node
    # 将节点node标记为已处理过
    processed.append(node)
    # 递归调用查找剩余节点
    node = find_lowest_cost_node(costs)

print(graph)
print(costs)
print(parents)

# 下面打印出节点X到节点Y的最短路径
# 直接遍历parents表
parent_node = parents['Y']
found = False
lowest_node_list = ['Y']
while not found:
    # print(parent_node)
    lowest_node_list.append(parent_node)
    if parent_node == 'X':
        found = True
    else:
        parent_node = parents[parent_node]
# 最终结果逆序：起点X-->终点Y
lowest_node_list.reverse()
print(lowest_node_list)
