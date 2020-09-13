# -*- coding: utf-8 -*-

import turtle

def draw_line(my_turtle, line_len):
    """
    使用海龟工具递归画图
    :param my_turtle:
    :param line_len:
    :return:
    """
    if line_len > 0:
        my_turtle.forward(line_len)
    my_turtle.right(90)
    draw_line(my_turtle, line_len - 1)


def draw_tree(my_turtle, line_len):
    """
    使用海龟工具递归画分形树
    :param my_turtle:
    :param line_len:
    :return:
    """
    if line_len > 10:
        my_turtle.forward(line_len)
        my_turtle.right(20)
        draw_tree(my_turtle, line_len - 15)
        my_turtle.left(40)
        draw_tree(my_turtle, line_len - 10)
        my_turtle.right(20)
        my_turtle.backward(line_len)

if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    # draw_line(my_turtle, 100)
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    # 设置画笔颜色
    my_turtle.color('green')
    draw_tree(my_turtle, 75)
    my_win.exitonclick()