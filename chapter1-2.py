# programming to solve growth problems and provide a diagrammatic analysis
# written by zhangqinag, last modified on 2016/03/28
from pylab import *
import pickle

N = []  #the list of the population
t = [0]  #the list of the time
a = 0   #the parameter a
b = 0   #the parameter b
dt = 0  #the time step
f = 1000  #the precision

#receive input paradise and calculate a suitable end time
def initialize(N, t,_a,_b):
    global a,b
    N.append(float(raw_input("initial populatin -> ")))
    a= float(raw_input("constant a -> "))
    b= float(raw_input("constant b -> "))
    return 0

## calculate the N and t every moment
def calculate(N, t, a, b, f, dt):
    print N
    print a
    print b
    print t
    print dt
    print f
    
    if a/b<N[0]:
       dt=N[0]/10000/(b*N[0]-a)/b
    elif a/b>N[0]:
       dt=N[0]/100.0/(a-b*N[0])
    else:
       dt=0.1
    for i in range(1, f):
        N.append(N[i - 1] + a*N[i - 1]*dt -N[i - 1]*N[i - 1]*b*dt)
        t.append(t[i - 1] + dt)
    return 0

#save the results
def store(N, t, f):
    mfile = open("notes.txt2", "a")
    for i in range(f):
        print >> mfile, t[i], N[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(N, pickle_file)

    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print N

initialize(N,t, a, b)
calculate(N, t, a, b, f,dt)
store(N, t, f)

#draw the asymptote
ymin=min(N)
ymax=max(N)
xmin, xmax = min(t), max(t)
if a >= b*N[0]:
    plot([0,xmax],[ymax,ymax],label='the terminal population', color='red',    linewidth=2.5, linestyle="--")
else:
    plot([0,xmax],[ymin,ymin],label='the terminal population', color='red',    linewidth=2.5, linestyle="--")

#adjust the diagram
xmin, xmax = min(t), max(t)
ymin, ymax = int(min(N)), round(max(N))

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
ylabel('the population N')
xlabel('the time t')

# add label
xticks([xmin, xmax])
yticks([ymin, ymax/2, ymax],[ymin, ymax/2, ymax])

#draw the diagram
plot(t, N, label='population growth model')
legend(loc='upper center')
show()
savefig("test_.jpg")

read()
