#chapter1 description

##摘要
关于书上习题1.3，关于在与速度成正比的阻力一恒力的作用下的动力学问题的解决方案

##背景介绍
在与速度成正比的阻力一恒力的作用下的动力学方程可以由下面的方程描绘
![](http://www.sciweavers.org/upload/Tex2Img_1458640335/render.png)

##正文
1.该运动方程用泰勒展开后可以近似表示为<br> ![](http://www.sciweavers.org/upload/Tex2Img_1458640602/render.png)
  当我们把时间间隔去的十分小的时候就能有很好的近似结果<br>
2.参数设置
  所有蚕食都是由用户根据自己的实际情况设置，程序运行时会提示用户输入要输入的参数<br>
3.绘制图表的工具为matplotlib<br>
4.源代码地址 [chapter1.py](https://github.com/zqbinggong/computational-physics_N2013301020039/blob/master/chapter1.py) <br>
5.效果展示<br>
  按照书上的推荐，设置a=10，b=1，取v=100，dt=0.1，t=100
  ![](http://imgsrc.baidu.com/forum/pic/item/043dc08ba61ea8d3e61e59b7900a304e241f588f.jpg)     当时间趋于无穷大时，速度将趋于不变，即terminal speed

##结论
  此程序节本能够完成书上习题的要求
 
##致谢
感谢刘文焘同学在调整坐标轴刻度时提供的帮助！
