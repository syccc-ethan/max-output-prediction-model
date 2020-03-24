# max-output-prediction-model
## 分布式综合智慧能源系统模型——最大出力预测模型

===========================<br>
### 项目简述
为有效推动能源清洁生产和就近消纳,提高整个区域能源系统的能源利用率、经济性与稳定性,达到节能环保的目的,提出了分布式智慧能源系统构架,实时识别区域能源数据并进行可视化处理，以实现区域内各类分布式能源系统进行多能互补、优化调度。
### 功能简介
1、利用以cv2为主的第三方库函数对输入图像进行降噪、归一化、区域搜索等处理。<br>
2、基于卷积神经人工智能网络进行实时图像的处理与识别。<br>
3、通过灰色模型、bp神经网络模型等手段进行电力系统最大出力的预测。<br>
4、利用qt实现将各功能集成为可视化图形界面。<br>
### 环境依赖
Python 环境搭建<br>
Qt图形用户界面开发框架<br>
mysql数据库环境<br>

### python第三方库
absl-py==0.7.1<br>
asgiref==3.2.3<br>
astor==0.8.0<br>
bleach==1.5.0<br>
certifi==2019.6.16<br>
chardet==3.0.4<br>
cvxopt==1.2.3<br>
cycler==0.10.0<br>
Cython==0.29.13<br>
Django==3.0.1<br>
djangorestframework==3.11.0<br>
...<br>
详见requirement.txt

### 输入参数要求
oee_data输入数据示例：'2018-06-25', '90', '90', '90', '86', '90', '90', '90', '85', '90', '90', '80'<br>
loss输入数据示例：'2018-06-22', '50', '40', '20', '30', '10', '20'<br>
dz输入数据实例：'2018-06-23 07:32:57', '1A', '0A', 'action3', 'start'<br>
SJC要求为datetime<br>
GRGH、LJGH、FLAG均为最高20字节字符

### 视频输入
在本项目中，在线视频和本地视频数据源的读取处理均可实现，且都要求双数据源（左右摄像头）的输入。本地视频要求MP4格式。

### 目录结构描述
├── Readme.md                   // help<br>
├── question                    // 问题<br>
├── data                        // 数据<br>
│   ├── data_access.py         // 数据获取<br>
│   ├── test.sql               // 测试数据<br>

├── figure                      // 图表<br>
│   ├── figure_plot.py         // 图表绘制<br>
├── maindo                         // 主程序<br>
│   ├── xio_all.py         // 主应用<br>
│   ├── xio_figureplot.py         // 图表绘制<br>
│   ├── xio_playvideo.py          // 读取视频数据流<br>
│   ├── xio_server.py             //远程服务器连接<br>
│   ├── xio_shumei.py             // 数据传输与管理<br>

├── uidesign                        //各模块UI设计<br>
├── uifiles                         //各模块UI设计参数<br>
├── utils                           // 辅助工具<br>
│   ├── utils.py         // 视频图像处理工具<br>
│   ├── vision.py         // 图像识别工具<br>





王波波，宋伟，李天昊，汤俊萱，孙奕程

东华大学，上海视易信息技术有限公司，2020

