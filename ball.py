#programming to stimulate the movement of a ball between two floor
#programming by zhangqiang, last modified on 2016/03/29

from visual import *
scene.autoscale = False  
  
#two floor are instances of box object with attributes like length, height, width etc.  
floor1 = box(pos=vector(0,5,0),length=4, height=0.5, width=4, color=color.red)  
floor2 = box(pos=vector(0,-5,0),length=4, height=0.5, width=4, color=color.red) 
  
# A ball is a spherical object with attributes like position,radius, color etc..  
ball = sphere(pos=(0,0,0),radius=1, color=color.blue)  
  
#Ball moves in the y axis with a initial velocity  
ball.velocity = vector(0,-9,0)  
  
# small change in time  
dt = 0.01  
  
while 1:  
    #setting the rate of animation speed  
    rate(100)  
    # Change the position of ball based on the velocity on the y axis  
    ball.pos = ball.pos + ball.velocity*dt  
    if ball.pos.y > 4.0:  
        ball.velocity.y = -ball.velocity.y  
    elif ball.pos.y < -4.0:  
        ball.velocity.y = -ball.velocity.y    
    else:  
        ball.velocity.y = ball.velocity.y - 9.8*dt  #move with gravitation
