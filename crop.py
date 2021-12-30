"""图像裁剪工具
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def crop2048x2048(img):
    """裁剪2048x2048的图像为两张1024x1024的图像（去除黑色区域）

    Args:
        img (np.ndarray): 传入一个二维numpy数组

    Returns:
        np.ndarray: 上半段图像
        np.ndarray: 下半段图像 
    """
    img = img[:, 500:500+1024]
    return img[0:1024, :], img[1024:,:]

def crop1024xN(img):
    """裁剪较长的图像为多张1024x1024的图像

    Args:
        img (np.ndarray): 二维numpy数组，代表一张图片

    Raises:
        AttributeError: 传入图像宽度应为1024，否则触发

    Returns:
        list: 裁剪后的图像列表
    """
    height, width = img.shape[0], img.shape[1]
    if width != 1024:
        raise AttributeError("Width is not 1024!")

    num = int(height / width)
    img_list = []
    for i in range(num-1):
        img_list.append(img[1024*i:1024*(i+1), :])
    img_list.append(img[1024*(num-1):, :])
    return img_list

def crop2single(jpg_path):
    img = cv.imread(jpg_path, cv.IMREAD_GRAYSCALE)
    height, width = img.shape[0], img.shape[1]
    if height == 1024 and width == 1024:
        return
    if height == 2048 and width == 2048:
        img_list = crop2048x2048(img)
    if width == 1024:
        img_list = crop1024xN(img)
    for i, im in enumerate(img_list):
        cv.imwrite(jpg_path[:-4] + str(i) + '.jpg', im)

crop2single('data/000.jpg')