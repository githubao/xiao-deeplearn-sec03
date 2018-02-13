#!/usr/bin/env python
# encoding: utf-8 

"""
@description: 分类

@author: pacman
@time: 2018/1/5 11:35
"""

import numpy as np
import matplotlib.pyplot as plt


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def run():
    x = np.array([3, 2, 1])
    y = softmax(x)
    print(y)


def sum_example():
    """
    axis 可以根据是哪个数字，数到加和哪个方括号里面的数据
    :return:
    """
    arr = np.array([[1, 2], [3, 4]])
    print(np.sum(arr, axis=0))
    print(np.sum(arr, axis=1))
    print(np.sum(arr))


def vstake_example():
    """
    one_like: 与输入维度相同，但是元素数值都变成１
    hstack vstack 竖着或者横着接起来，数组的维度不变
    stack 直接接起来，数组维度增加一维
    :return: 
    """
    x = np.array([[1, 2], [3, 4]])
    # one_like = np.ones_like(x)
    # print(one_like)

    print(np.vstack([1, 2, 3]))
    print(np.vstack(([1, 2, 3], [4, 5, 6])))
    print(np.vstack(([[1, 11], [2, 22], [3, 33]], [[2, 22], [3, 33], [4, 44]])))
    print(np.hstack(([[1, 11], [2, 22], [3, 33]], [[2, 22], [3, 33], [4, 44]])))
    print(np.stack(([[1, 11], [2, 22], [3, 33]], [[2, 22], [3, 33], [4, 44]])))


def vstake_example2():
    print(np.vstack([[1, 2], [3, 4], [5, 6]]))
    print(np.array([[1, 2], [3, 4], [5, 6]]))
    # print(np.vstack([[1, 2], [3, 4], [5, 6]]))


def plot():
    x = np.arange(-2.0, 6.0, 0.1)
    # x = np.arange(-2.0, 6.0, 1)
    print(x)
    print(x.shape)

    y = np.array([[1, 2, 3], [4, 5, 6]])
    print(y)
    print(y.shape)

    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

    plt.plot(x, softmax(scores).T, linewidth=2)
    plt.show()


def main():
    # run()
    # sum_example()
    vstake_example()
    # plot()


if __name__ == '__main__':
    main()
