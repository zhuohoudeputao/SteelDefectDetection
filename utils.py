import numpy as np
import matplotlib.pyplot as plt

def rotate_img(img: np.ndarray):
    """预处理1. 假定焊缝是在图像中间区域，如果不是则需要对图像进行旋转。
    原理：取图片最中间的一行一列，通过其方差进行判断，如果是正确的方向，那么行方差应该比列方差更大

    Args:
        img (np.ndarray): 已经做过对比度处理的图像

    Returns:
        [np.ndarray]: 处理后的图像
    """
    height, width = img.shape
    margin = 100
    center_line = img[height // 2, margin:-margin] # 边界可能出现亮边或黑边
    center_column = img[margin:-margin, width // 2]
    line_std = np.std(center_line) # 行方差
    column_std = np.std(center_column) # 列方差
    # print(column_std, line_std)
    if column_std > line_std:
        img = img.T # 转置
        img = img[:, ::-1] # 翻转
    
    return img

def flip_color(img: np.ndarray) -> np.ndarray:
    """预处理2. 假定焊缝是较暗的区域，也即其灰度值较低，如果不是则需要进行反转。
    原理：取图片最中间的一行，通过其灰度均值进行判断，如果整体偏暗，说明中间应该是偏亮的，需要反转

    Args:
        img (np.ndarray): 已经做过对比度处理和旋转处理的图像

    Returns:
        np.ndarray: 处理后的图像
    """
    height, width = img.shape
    margin = 100
    center_line = img[height // 2, margin:-margin]
    mean_val = np.mean(center_line)
    if mean_val < 127:
        img = 255 - img
    return img

def weld_extract(img: np.ndarray) -> np.ndarray:
    """焊缝区域提取。
    原理： 
        1. 统计每行灰度波谷的位置，从而确定焊缝大致位置；
        2. 对焊缝大致位置进行再一次的细分查找，得到更加精细的位置；

    Args:
        img (np.ndarray): 已经做过对比度处理、旋转处理和颜色翻转的图像

    Returns:
        np.ndarray: 截取后的图像
    """
    height, width = img.shape
    margin = 100
    img2 = img[:, margin:-margin]
    # 每行的灰度波谷
    line_lowest = [np.argmin(img2[i, :]) for i in range(height)]
    # plt.figure()
    # plt.hist(line_lowest)
    # plt.show()
    # 确定焊缝大致位置
    sum, pos = np.histogram(line_lowest) # 统计出现波谷的位置
    max_pos = np.argmax(sum)
    # 对中间区域细分查找,确定更精确的位置
    sum, pos = np.histogram(line_lowest, bins=20, range=(pos[max_pos], pos[max_pos+1])) 
    max_pos = np.argmax(sum)
    # 确定焊缝中间位置
    center = int(pos[max_pos+1])
    # plt.figure()
    # plt.imshow(img2, cmap='gray')
    # plt.plot([center]*height, np.arange(height))
    # plt.legend(['center'])
    # plt.show()

    # 计算需要裁剪的量,这里还有优化空间
    line_width = 70
    img3 = img2[:, center-line_width: center+line_width]
    return img3

def detect_point(img: np.ndarray):
    """检测斑点位置

    Args:
        img (np.ndarray): 
    """
    height, width = img.shape
    # 按列检测方差
    stds = []
    for j in range(width):
        column = img[:, j]
        stds.append(np.std(column))
    
    maxstdpos = np.argmax(stds)
    if np.max(stds) < 10: # 当分布都比较均匀时，说明没有哪一列的方差突然变大了，正常
        print('The weld is normal.')
        return
    plt.plot(stds)

    column_err = img[:, maxstdpos]
    widthpos = np.argmax(column_err) # 出现错误的列的亮斑位置
    plt.figure()
    plt.plot(column_err)

    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.plot([maxstdpos]*height, np.arange(height))
    # # plt.plot([maxstdpos], [widthpos], '+')
    # box_width = 25
    # plt.plot([maxstdpos+box_width] * (box_width * 2), np.arange(widthpos-box_width, widthpos+box_width), 'r')
    # plt.plot([maxstdpos-box_width] * (box_width * 2), np.arange(widthpos-box_width, widthpos+box_width), 'r')
    # plt.plot(np.arange(maxstdpos-box_width, maxstdpos+box_width), [widthpos + box_width] * (box_width * 2), 'r')
    # plt.plot(np.arange(maxstdpos-box_width, maxstdpos+box_width), [widthpos - box_width] * (box_width * 2), 'r')
    plt.show()