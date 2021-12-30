"""dicom格式到jpg的转换
"""

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def dicom2jpg(file_path):
    ds = pydicom.dcmread(file_path)
    ds.SamplesPerPixel=1 # 读出来只有一半的数据，但是SamplesPerPixel却有两个
    # im = ds.pixel_array.T[3008*3:3008*3+3008, :]
    im = ds.pixel_array.T
    im = im / np.max(im) * 255 # 归一化到0-255， 原本图像的值非常大
    cv.imwrite(file_path[:-4] + '.jpg', im) # 保存图像
    rows, columns = ds.Rows, ds.Columns
    print(rows, columns)
    plt.imshow(im, cmap='gray') # 展示图像
    plt.show()

dicom2jpg('data/00058_original.dcm')