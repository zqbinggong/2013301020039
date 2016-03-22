# programming to solve fall-with-resistance model and provide a diagrammatic analysis
# written by zhangqinag, last modified on 2016/03/22
from pylab import *
import pickle

v = []
t = []
a = 0
b = 0
dt = 0
n = 0

#receive input paradise and calculate a suitable end time
def initialize(v, t, _a, _b, _dt, _n):
    global a,b, dt, n
    v.append(float(raw_input("initial speed -> ")))
    a= float(raw_input("constant a -> "))
    b= float(raw_input("constant b -> "))
    dt = float(raw_input("time step -> "))
    time = float(raw_input("total time -> "))
    t.append(0)
    n = int(time/dt)
    return 0

## calculate the v and t every moment
def calculate(v, t, a, b, dt, n):
    print v
    print a
    print b
    print t
    print dt
    print n
    for i in range(1, n):
        v.append(v[i - 1] + a*dt -v[i - 1]*b*dt)
        t.append(t[i - 1] + dt)
    return 0

#save the results
def store(v, t, n):
    mfile = open("notes.txt", "a")
    for i in range(n):
        print >> mfile, t[i], v[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(v, pickle_file)

    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print v

initialize(v, t, a, b, dt ,n)
calculate(v, t, a, b, dt, n)
store(v, t, n)

#draw the asymptote
ymin=min(v)
ymax=max(v)
v_t= ymin
plot([0,ymax],[v_t,v_t],label='the terminal speed', color='red', linewidth=2.5, linestyle="--")

#adjust the diagram
xmin, xmax = min(t), max(t)
ymin, ymax = int(min(v)), round(max(v))

dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + 2 * dy)

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#name the label
ylabel('the spped v')
xlabel('the time t')

#draw the diagram
plot(t, v, label='free fall with resistance')
legend(loc='upper center')
show()
savefig("test_.jpg")

read()
