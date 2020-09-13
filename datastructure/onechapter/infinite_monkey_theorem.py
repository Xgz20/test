# 无限猴子定理，
# 该定理指出，猴子随机在打字机键盘键入一个字符，经过无限时间后，
# 肯定会键入一系列给定的文字，比如莎士比亚全集。好吧，假设我们用一个Python 函数替换猴子。
# 你认为多久以后才能生成一句莎士比亚的名言呢？我们将这句话定为：“methinks it is a weasel”。

# 算法：
# 我们将模拟这个问题的方法是编写一个函数，该函数生成一个27 个字符长度的字符串，
# 从26 个字母和空格中随机选择一个字符。我们将编写另一个函数，来比较随机生成的字符串和目标字符串。
# 第三个函数将反复调用生成和比较函数，那么如果所有目标字母都在随机字符串中出现了，我们就完成了。
# 如果字母没有全部出现，我们会生成一个全新的字符串.为了让它更易于跟随你的程序的过程，
# 第三个函数应该返回出到目前为止产生的最好的字符串，并返回在产生这个字符串之前每1000次尝试中产生其它不合题意的字符串的次数。

import random,logging,time

logging.basicConfig(level=logging.INFO)

# 从26个字母和空格字符中随机抽出组成一个长度为23的字符串
def generateRandomStr():
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','']
    result_str = ''
    for i in range(23):
        result_str = result_str + char_list[random.randint(0,26)]
    logging.info(result_str)
    return result_str

# 比较随机生成的字符串和默认字符串的匹配程度，如果完全匹配，则直接返回一个元组（True，count）
# 如果不是完全匹配则返回元组（False，count），其中count表示有几个字符匹配
def compareStr(randomStr, defaultStr):
    count = 0
    for i in range(23):
        if randomStr[i] == defaultStr[i]:
            count = count + 1
        else:
            return (False, count)
    if count == 27:
        return (True, count)

# 在规定次数内，随机生成字符串，并与默认字符串做对比
def compute(defaultStr):
    record_dict = {}
    # time.
    max_count = 0
    flag = 0
    max_matching_str = ''
    for i in range(1000):
        random_str = generateRandomStr()
        temp_tuple = compareStr(random_str, defaultStr)
        logging.info(temp_tuple)
        if temp_tuple[0]:
            return [temp_tuple[1], random_str, i]
        else:
            if max_count < temp_tuple[1]:
                max_count = temp_tuple[1]
                flag = i
                max_matching_str = random_str
    return [max_count, max_matching_str, flag]



if __name__ == '__main__':
    default_str = 'methinks it is a weasel'
    result_list = compute(default_str)
    print(result_list[0])
    print(result_list[1])
    print(result_list[2])










