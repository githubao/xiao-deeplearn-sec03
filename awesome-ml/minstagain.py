#!/usr/bin/env python
# encoding: utf-8

"""
@description: 再次写minst，但是这次数据不是minst

@author: pacman
@time: 2018/2/13 18:04
"""

import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
import pickle
from sklearn.linear_model import LogisticRegression

url = 'http://comondatastorage.googleapis.com/books1000/'
last_percent_reported = None
data_root = './file'


def download_progress_hook(count, block_size, total_size):
    global last_percent_reported
    percent = int(count * block_size * 100 / total_size)

    if last_percent_reported != percent:
        if percent % 5 == 0:
            sys.stdout.write('{}%'.format(percent))
            sys.stdout.flush()
        else:
            sys.stdout.write('.')
            sys.stdout.flush


def main():
    print('do sth')


if __name__ == '__main__':
    main()
