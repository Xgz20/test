# 定义一个分数类型，支持分数的加减乘除等常用数据操作

import logging

logging.basicConfig(level=logging.INFO)



# 辗转相除法求两个数的最大公约数
def gcd(m, n):
    if m == 0 or n == 0:
        print('请输入两个不为0的整数！')
    a = m
    b = n
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        c = a % b
        a = b
        b = c
    logging.info(a)
    return a

# 相减法求最大公约数
def gcd2(m, n):
    a = m
    b = n
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    logging.info(a)
    return a

class Fraction(object):
    def __init__(self, molecule, denominator):
        self.molecule = molecule
        self.denominator = denominator
        if not (isinstance(self.molecule, int) or isinstance(self.denominator, int)):
            raise ValueError('input value is not integer')

    # 重写字符串输出
    def __str__(self):
        return str(self.molecule) + '/' + str(self.denominator)

    # 重写加法
    def __add__(self, other):
        new_molecule = self.molecule * other.denominator + self.denominator * other.molecule
        new_denominator = self.denominator * other.denominator
        max_com_divisor = gcd(new_molecule, new_denominator)
        return Fraction(new_molecule / max_com_divisor, new_denominator / max_com_divisor)

    # 重写减法
    def __sub__(self, other):
        new_molecule = self.molecule * other.denominator - self.denominator * other.molecule
        new_denominator = self.denominator * other.denominator
        max_com_divisor = gcd(new_molecule, new_denominator)
        return Fraction(new_molecule / max_com_divisor, new_denominator / max_com_divisor)

    # 重写乘法
    def __mul__(self, other):
        new_molecule = self.molecule * other.molecule
        new_denominator = self.denominator * other.denominator
        max_com_divisor = gcd2(new_molecule, new_denominator)
        return Fraction(new_molecule / max_com_divisor, new_denominator / max_com_divisor)

    # 重写除法
    def __truediv__(self, other):
        new_molecule = self.molecule * other.denominator
        new_denominator = self.denominator * other.molecule
        max_com_divisor = gcd2(new_molecule, new_denominator)
        return Fraction(new_molecule / max_com_divisor, new_denominator / max_com_divisor)

    # 重写equal方法
    def __eq__(self, other):
        cross_result1 = self.molecule * other.denominator
        cross_result2 = self.denominator * other.molecule
        return cross_result1 == cross_result2



if __name__ == '__main__':
    f1 = Fraction(2,3)
    f5 = Fraction(2,3)
    f2 = Fraction(4,5)
    # print(f1 + f2)
    f3 = Fraction(3,4)
    f4 = Fraction(1,4)
    # print(f3 - f4)
    # print(f1 * f2)
    # print(f1/f2)
    print(f1 == f5)