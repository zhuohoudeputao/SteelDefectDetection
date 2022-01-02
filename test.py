"""用于测试各个部分是否正常工作
"""
import cv2 as cv
from matplotlib import pyplot as plt
from utils import *

import unittest as ut

path_list = [
    'data/001_left.jpg',
    # 'data/001.jpg',
    # 'data/0001.jpg',
    # 'data/0002.jpg',
    # 'data/00003_original.jpg',
    # 'data/00004_original.jpg',
    # 'data/00005_original.jpg',
    # 'data/0003.jpg',
    # 'data/0004.jpg',
    # 'data/0005.jpg',
    # 'data/0006.jpg',
    # 'data/0007.jpg',
    # 'data/0008.jpg',
    # 'data/0009.jpg',
]

class TestCases(ut.TestCase):

    def test_rotate_img(self):
        for path in path_list:
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            img = cv.equalizeHist(img)
            img = rotate_img(img)
            plt.figure()
            plt.imshow(img, cmap='gray')
            plt.title(path)
            plt.show()
    
    def test_flip_color(self):
        # 必须在rotate_img处理完之后测试才有意义
        for path in path_list:
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            img = cv.equalizeHist(img)
            img = rotate_img(img)
            img = flip_color(img)
            plt.figure()
            plt.imshow(img, cmap='gray')
            plt.title(path)
            plt.show()
        
    def test_weld_extract(self):
        for path in path_list:
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            img = cv.equalizeHist(img)
            img = rotate_img(img)
            img = flip_color(img)
            img = weld_extract(img)
            plt.figure()
            plt.imshow(img, cmap='gray')
            plt.title(path)
            plt.show()
    
    def test_detect_point(self):
        for path in path_list:
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            img = cv.equalizeHist(img)
            img = rotate_img(img)
            img = flip_color(img)
            img = weld_extract(img)
            detect_point(img)