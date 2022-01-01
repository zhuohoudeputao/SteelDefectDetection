# SteelDefectDetection

钢材缺陷检测

## 环境配置

### Python3安装

Windows系统下，需要到[https://www.python.org/downloads/](https://www.python.org/downloads/) 下载安装包进行安装。

### 项目配置

首先使用git clone项目到本地

```shell
git clone https://github.com/zhuohoudeputao/SteelDefectDetection.git
```

此时执行上述语句的目录会新增一个SteelDefectDetection目录，cd进入该目录，安装依赖项

```shell
python3 -m pip install -U -r requirements.txt
```

然后就可以愉快地开始浏览代码和开发工作了。

## 数据

从数据来说，我们一开始获得的数据应该是.his文件或者.dicom文件，转换后得到的应该是1024x1024大小的钢管焊缝图，因此数据预处理部分需要的任务是

* [x] 格式转换，包括.his和.dcm两种格式文件转换为jpg文件
  
  * [x] his文件格式同dcm文件，都是DICOM标准的文件，使用Pydicom处理即可
  * [x] dcm文件格式已经可以做初步处理，但是仍然有部分看起来是黑色的，不知道为啥会有这种情况
* [ ] 图像裁剪
  
  * [ ] 现有大部分图像是1024x1024的，且钢材焊缝在中间位置
  * [ ] 部分图像的大小并不是完全是方形
* [ ] 数据标签
  
  * [ ] 从数据当中提取相应标签与数据关联

## 单幅钢材图片处理

1. 使用灰度值分布直方图，观察结果是：
   1. 可以使用一个较高的过滤值过滤掉
2. 

## 文献调研

| 引用 | 主要内容 |
| --- | --- | 
|[1]李金燕,李春祥,王锡岭.焊缝缺陷图像特征提取的研究[J].焊接技术,2018,47(11):78-82+6.DOI:10.13846/j.cnki.cn12-1070/tg.2018.11.023.  | 通过平滑滤波预和模糊增强预处理图像，通过阈值法分割背景和主要目标，再采用8连通区域判别法进行缺陷分割，最终计算缺陷的特征用于分类 |  
|  |  |


