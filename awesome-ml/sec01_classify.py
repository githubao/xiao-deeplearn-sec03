#!/usr/bin/env python
# encoding: utf-8 

"""
@description: 分类

@author: pacman
@time: 2018/1/5 11:35
"""

import numpy as np


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


def main():
    # run()
    sum_example()


if __name__ == '__main__':
    main()
