
# 牛顿逼近平方根，这里采用计算20次
def my_sqrt(value):
    root = float(value) / 2
    for n in range(20):
        root = (1/2) * (root + value / root)
    return root

if __name__ == '__main__':
    # input_value = input('please input:')
    print(my_sqrt(9))