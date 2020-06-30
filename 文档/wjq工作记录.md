# Day1
## 需求分析
分析系统的属性=
## 准备Ubuntu操作系统
之前安装的Windows+Ubuntu双系统
版本：
Linux的内核版本为#30~18.04.1-Ubuntu SMP Fri Jan 17 06:14:09 UTC 2020，发行版本为Ubuntu 18.04.4 LTS（Bionic Beaver）
## 搭建计算机视觉开发环境
1. 安装Anaconda。Anaconda集成了Python环境以及Python常用的数百个库.
2. 创建虚拟环境
确保Terminal仍然进入了anaconda3的bin目录下
```bash
 ./conda create -n tensorflow python=3.6 anaconda
```
其中虚拟环境的名字叫tensorflow，使用的Python版本是3.6。

执行此条命令后，Anaconda会复制一个一模一样的Python环境，所以执行时间较长，请耐心等待。
命令执行结束后， 输入下行命令将虚拟环境切换到刚创建的tensorflow下。

```bash
source activate tensorflow
```



3. 安装opencv库

Opencv是非常强大且简单的图像处理库。

首先确保Terminal仍然在tensorflow虚拟环境下，敲入如下2条命令安装opencv库。

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python==3.4.4.19
 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python==3.4.4.19
```
4. 安装深度学习框架TensorFlow库

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==1.12.0
```
5. 安装keras库

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple keras==2.2.4

```
6.安装dlib库

dlib库是人脸识别最重要最有名气的库。



## 遇到的问题
###  安装发生timeout
解决：换源
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python==3.4.4.19
 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python==3.4.4.19
```
