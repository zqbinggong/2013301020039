#cahpter1(2) description

##摘要
chapter1第二次作业选取了书上的习题1.6，关于人口增长问题的数值求解和结果分析。

##背景介绍
关于人口增长可以用方程![](http://imgsrc.baidu.com/forum/pic/item/579e672dd42a283488961bb75cb5c9ea14cebfa5.jpg)来描述，其中N为人口数量，a,b为相关参数，方程右边第一项对应于出生的人口，第二项对应于死亡的人口。易知a=bN时，人口趋于稳定。

##正文
1.该运动方程用泰勒展开后可以近似表示为![](http://imgsrc.baidu.com/forum/pic/item/6918cfb1cb134954017cc4d8514e9258d0094a76.jpg)
当我们将dt取得比较小时将会有很好的近似结果 <br>

2.参数设置<br>
——所有参数都是由用户根据实际情况设置，程序运行时会提示用户输入相关参数，包括a,b,N <br>
——参数的值对结果的影响是十分大的。容易看出，当a/b>N时，人口数量是递减的，当a/b < N时，人口的数量是递增的。<br>
——在计算过程中dt的值也必须由参数来决定，因为对于不同的参数，需要的dt的值不同。例如当a/b<< N时，dt应该特别小，否则会出现N<0而导致程序无法进行，而当a>>bN,时，当dt过小。则画出的曲线增长不明显。因此这里，根据不同的参数来设置dt，具体做法如下<br> ![](http://imgsrc.baidu.com/forum/pic/item/b083a9f81a4c510f9dc15da16759252dd52aa54f.jpg)

3.绘制图形的工具是matplotlib <br>

4.源代码地址 [chapter1-2.py](https://github.com/zqbinggong/computational-physics_N2013301020039/blob/master/chapter1-2.py) <br>

5.效果展示
a.取N=10，a=10,b=3 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=f2a567bda8c379317d688621dbc5b784/0dee6ff5e0fe99253664cceb33a85edf8cb1716c.jpg) <br>
b.取N=100，a=bN=10,b=0.1 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=f1af12895dafa40f3cc6ced59b65038c/aad1bffaaf51f3de36d01cdf93eef01f3b297976.jpg) <br>
c. N=1000，a=10,b=3 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=ae1c3dc0d61373f0f53f6f97940e4b8b/4101e5efce1b9d1682a53fdaf4deb48f8d546476.jpg) <br>
d.N=5,a=0.2,b=0.01 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=7cb83bef044f78f0800b9afb49300a83/bb93d6eef01f3a29aaa070759e25bc315d607c6c.jpg)

##结论
  人口增长或者衰减到一定值时，会趋于稳定值a/b，这符合现实规律。
 
##致谢
