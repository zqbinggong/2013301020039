#programming to study the realistic projectile motion
#written by zhangqiang,last modedied on 2016/06/19
import sys
import math
import time
import numpy 
from matplotlib import pyplot 
from matplotlib import animation
from pylab import *
# some paremeters and initial information
g = 9.8
B2m = 4e-5
initSpeed = 1000.0
hit_area = float(raw_input('please input the hit_area : '))
x_t = float(raw_input('please enter the distance of the target : '))
y_t = float(raw_input('please enter the height of the target : '))
d = float(raw_input('please enter 0 for isothermal gas or 1 for adiabatic gas : '))   #to determine the approximation approach
sita = math.pi / 2
sign = -2


class FlightState:

    def __init__(self, _x=0., _y=0., _v_x=0., _v_y=0., _t=0.):
        self.x  = _x
        self.y  = _y
        self.v_x = _v_x
        self.v_y = _v_y
        self.t  = _t


class CannonShell:

    def __init__(self, _fs=FlightState(), _dt=0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt

    def getNextState(self):
        currentState = self.flightState[-1]
        x  = currentState.x + currentState.v_x * self.dt
        y  = currentState.y + currentState.v_y * self.dt
        v_x = currentState.v_x + self.getCurrentAcc(currentState)[0] * self.dt
        v_y = currentState.v_y + self.getCurrentAcc(currentState)[1] * self.dt
        self.flightState.append(FlightState(x, y, v_x, v_y, currentState.t + self.dt))

    def getCurrentAcc(self, currentState):
        factor = self.getFactor(currentState)
        a_x = factor * (-B2m * currentState.v_x**2)
        a_y = factor * (-B2m * currentState.v_y**2) - g
        currentAcc = [a_x, a_y]
        return currentAcc

    def getFactor( self,currentState):
        alpha = 2.5
        a = 6.5e-3
        factor = 0
        try:
            factor = d*(1 - a * currentState.y / 288.15)**alpha+(1-d)*math.exp(-currentState.y/10000.0)
        except ValueError, e:
            print e
        return factor


def calculate(target):
    initState = FlightState(0., 0., initSpeed * math.cos(sita), initSpeed * math.sin(sita))
    cannonShell = CannonShell(initState, 1)
    while True:
        if cannonShell.flightState[-1].y < target[1] and cannonShell.flightState[-1].v_y < 0:
            dy = cannonShell.flightState[-1].y - target[1]
            tanB = cannonShell.flightState[-1].v_x / cannonShell.flightState[-1].v_y
            cannonShell.flightState[-1].x -= dy * tanB
            cannonShell.flightState[-1].y = target[1]
            break
        cannonShell.getNextState()
    return cannonShell


def storeData(target, accuracy):
    f = open("shootParadise.txt", "w")
    print >> f, "Target position:\n\tX: %f \n\tY: %f \n" % (target[0], target[1])
    print >> f, "Shooting angle: %f \nShooting Speed: %f\n" % (sita * 180 / math.pi, initSpeed)
    print >> f, "Attacking accuracy: %f " % (accuracy)
    f.close()


def shoot():
    print "sita: ", sita * 180 / math.pi
    print "initSpeed: ", initSpeed

trail_x, trail_y = [], []
farthest_x = 0
target = [x_t, y_t]
# target.append(float(raw_input("Please input the target's X_position: ")))
# target.append(float(raw_input("Please input the target's Y_position: ")))
# time.sleep(10)

fig = pyplot.figure(figsize=(15,6))
xmin, xmax = 0., 4e+4
ymin, ymax = 0., 1e+4
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.2
ax = pyplot.axes(xlim=(xmin, xmax + dx), ylim=(ymin, ymax + dy))
line, = ax.plot([], [])


# draw the cannon
pyplot.plot([x_t-200,x_t-200], [y_t-50,y_t+50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t+200,x_t+200], [y_t-50,y_t+50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t-200,x_t+200], [y_t-50,y_t-50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t-200,x_t+200], [y_t+50,y_t+50], color='blue', linewidth=5, linestyle="-")
# add auxiliary line
pyplot.plot([0,xmax], [target[1],target[1]], color='red', linewidth=2.5, linestyle="--")
pyplot.plot([target[0],target[0]], [0,ymax], color='red', linewidth=2.5, linestyle="--")

# name the axis
pyplot.xlabel(r'$x(m)$', fontsize=16)
pyplot.ylabel(r'$y(m)$', fontsize=16)

# draw animation
def initAnimation():   
    line.set_data([], [])
    return line,

def animate(i):
    global sign, sita, initSpeed, hit_area, farthest_x, trail_x, trail_y
    x, y = [], []
    cannonShell = calculate(target)
    for flightState in cannonShell.flightState:
        x.append(flightState.x)
        y.append(flightState.y)
    if sign == -2:
        sita -= math.pi / (2 * 300)
        if farthest_x < cannonShell.flightState[-1].x:
            farthest_x = cannonShell.flightState[-1].x
        else:
            sign = -1
    elif sign == -1:
        accuracy = math.fabs(cannonShell.flightState[-1].x - target[0])
        initSpeed -= math.sqrt(accuracy / 1000)
        if accuracy < hit_area:
            shoot()
            storeData(target, accuracy)
            sign = 0
    else:
        try:
            trail_x.append(cannonShell.flightState[sign].x)
            trail_y.append(cannonShell.flightState[sign].y)
            x, y = trail_x, trail_y
            sign += 1
        except IndexError:
            sys.exit(0)
    line.set_data(x, y)   
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=initAnimation, interval=20, blit=True)
pyplot.show()
'''
import sys
import math
import time
import numpy 
from matplotlib import pyplot 
from matplotlib import animation
from pylab import *
# some paremeters and initial information
g = 9.8
B2m = 4e-5
initSpeed = 1000.0
hit_area = float(raw_input('please input the hit_area : '))
x_t = float(raw_input('please enter the distance of the target : '))
y_t = float(raw_input('please enter the height of the target : '))
d = float(raw_input('please enter 0 for isothermal gas or 1 for adiabatic gas : '))   #to determine the approximation approach
sita = math.pi / 2
sign = -2


class FlightState:

    def __init__(self, _x=0., _y=0., _v_x=0., _v_y=0., _t=0.):
        self.x  = _x
        self.y  = _y
        self.v_x = _v_x
        self.v_y = _v_y
        self.t  = _t


class CannonShell:

    def __init__(self, _fs=FlightState(), _dt=0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt

    def getNextState(self):
        currentState = self.flightState[-1]
        x  = currentState.x + currentState.v_x * self.dt
        y  = currentState.y + currentState.v_y * self.dt
        v_x = currentState.v_x + self.getCurrentAcc(currentState)[0] * self.dt
        v_y = currentState.v_y + self.getCurrentAcc(currentState)[1] * self.dt
        self.flightState.append(FlightState(x, y, v_x, v_y, currentState.t + self.dt))

    def getCurrentAcc(self, currentState):
        factor = self.getFactor(currentState)
        a_x = factor * (-B2m * currentState.v_x**2)
        a_y = factor * (-B2m * currentState.v_y**2) - g
        currentAcc = [a_x, a_y]
        return currentAcc

    def getFactor( self,currentState):
        alpha = 2.5
        a = 6.5e-3
        factor = 0
        try:
            factor = d*(1 - a * currentState.y / 288.15)**alpha+(1-d)*math.exp(-currentState.y/10000.0)
        except ValueError, e:
            print e
        return factor


def calculate(target):
    initState = FlightState(0., 0., initSpeed * math.cos(sita), initSpeed * math.sin(sita))
    cannonShell = CannonShell(initState, 1)
    while True:
        if cannonShell.flightState[-1].y < target[1] and cannonShell.flightState[-1].v_y < 0:
            dy = cannonShell.flightState[-1].y - target[1]
            tanB = cannonShell.flightState[-1].v_x / cannonShell.flightState[-1].v_y
            cannonShell.flightState[-1].x -= dy * tanB
            cannonShell.flightState[-1].y = target[1]
            break
        cannonShell.getNextState()
    return cannonShell


def storeData(target, accuracy):
    f = open("shootParadise.txt", "w")
    print >> f, "Target position:\n\tX: %f \n\tY: %f \n" % (target[0], target[1])
    print >> f, "Shooting angle: %f \nShooting Speed: %f\n" % (sita * 180 / math.pi, initSpeed)
    print >> f, "Attacking accuracy: %f " % (accuracy)
    f.close()


def shoot():
    print "sita: ", sita * 180 / math.pi
    print "initSpeed: ", initSpeed

trail_x, trail_y = [], []
farthest_x = 0
target = [x_t, y_t]
# target.append(float(raw_input("Please input the target's X_position: ")))
# target.append(float(raw_input("Please input the target's Y_position: ")))
# time.sleep(10)

fig = pyplot.figure(figsize=(15,6))
xmin, xmax = 0., 4e+4
ymin, ymax = 0., 1e+4
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.2
ax = pyplot.axes(xlim=(xmin, xmax + dx), ylim=(ymin, ymax + dy))
line, = ax.plot([], [])


# draw the cannon
pyplot.plot([x_t-200,x_t-200], [y_t-50,y_t+50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t+200,x_t+200], [y_t-50,y_t+50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t-200,x_t+200], [y_t-50,y_t-50], color='blue', linewidth=5, linestyle="-")
pyplot.plot([x_t-200,x_t+200], [y_t+50,y_t+50], color='blue', linewidth=5, linestyle="-")
# add auxiliary line
pyplot.plot([0,xmax], [target[1],target[1]], color='red', linewidth=2.5, linestyle="--")
pyplot.plot([target[0],target[0]], [0,ymax], color='red', linewidth=2.5, linestyle="--")

# name the axis
pyplot.xlabel(r'$x(m)$', fontsize=16)
pyplot.ylabel(r'$y(m)$', fontsize=16)

# draw animation
def initAnimation():   
    line.set_data([], [])
    return line,

def animate(i):
    global sign, sita, initSpeed, hit_area, farthest_x, trail_x, trail_y
    x, y = [], []
    cannonShell = calculate(target)
    for flightState in cannonShell.flightState:
        x.append(flightState.x)
        y.append(flightState.y)
    if sign == -2:
        sita -= math.pi / (2 * 300)
        if farthest_x < cannonShell.flightState[-1].x:
            farthest_x = cannonShell.flightState[-1].x
        else:
            sign = -1
    elif sign == -1:
        accuracy = math.fabs(cannonShell.flightState[-1].x - target[0])
        initSpeed -= math.sqrt(accuracy / 1000)
        if accuracy < hit_area:
            shoot()
            storeData(target, accuracy)
            sign = 0
    else:
        try:
            trail_x.append(cannonShell.flightState[sign].x)
            trail_y.append(cannonShell.flightState[sign].y)
            x, y = trail_x, trail_y
            sign += 1
        except IndexError:
            sys.exit(0)
    line.set_data(x, y)   
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=initAnimation, interval=20, blit=True)
pyplot.show()
'''
