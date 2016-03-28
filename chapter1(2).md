#chapter1 description

##摘要
chapter1第二次作业选取了书上的习题1.6，关于人口增长问题的数值求解和结果分析。

##背景介绍
关于人口增长的问题可用方程
![](http://www.sciweavers.org/tex2img.php?eq=%20%5Cfrac%7BdN%7D%7Bdt%7D%3DaN-b%20N%5E%7B2%7D%20%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)来描述，其中N为人口数量，a,b为参数，方程右边第一项对应于增长的人口，右边第二项对应于死亡的人口。易知，当a=bN 时，人口将会稳定，不发生改变。

##正文
1.该运动方程用泰勒展开后可以近似表示为<br> ![](http://www.sciweavers.org/tex2img.php?eq=N%28dt%29%3DN%280%29%2BaN%280%29dt-b%20N%280%29%5E%7B2%7D%20dt&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  当我们把时间间隔去的十分小的时候就能有很好的近似结果<br>
2.参数设置
 　a.所有参数都是由用户根据自己的实际情况设置，程序运行时会提示用  户输入要输入的参数，包括a,b,N<br>
 　b.参数的值对计算的结果影响较大。很容易看出，当a>bN时，人口数量是递增的，当a< bN时，人口数量是递减的。
 　c.在计算过程中dt的值也必须由参数来确定，否则可能出现N<0的情况，导致程序出错。在这里我采用如下的方法来确定dt的取值![](http://imgsrc.baidu.com/forum/w%3D580/sign=28b90a811ed8bc3ec60806c2b28aa6c8/b083a9f81a4c510f9dc15da16759252dd52aa54f.jpg)
 　
3.绘制图表的工具为matplotlib<br>
4.源代码地址 [chapter1-2.py](https://github.com/zqbinggong/computational-physics_N2013301020039/blob/master/chapter1-2.py) <br>
5.效果展示<br>
  a.取N=10，a=10,b=3 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=f2a567bda8c379317d688621dbc5b784/0dee6ff5e0fe99253664cceb33a85edf8cb1716c.jpg)
  b.取N=100，a=bN=10,b=0.1 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=f1af12895dafa40f3cc6ced59b65038c/aad1bffaaf51f3de36d01cdf93eef01f3b297976.jpg)
  c. N=1000，a=10,b=3 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=ae1c3dc0d61373f0f53f6f97940e4b8b/4101e5efce1b9d1682a53fdaf4deb48f8d546476.jpg)
  d.N=5,a=0.2,b=0.01 ![](http://imgsrc.baidu.com/forum/w%3D580/sign=7cb83bef044f78f0800b9afb49300a83/bb93d6eef01f3a29aaa070759e25bc315d607c6c.jpg)
##结论
  人口增长或者衰减到一定值时，会趋于稳定，这符合现实规律。
 
##致谢
