#programming to stimulate teh Lorenz model
#writen by zhangqiang ,last modefied on 16/05/09
from numpy import * 
import matplotlib.pyplot as plt

  
class LORENZ(object):
    def __init__(self,_r=25,_dt=0.001,_time=50,_sigma=10,_b=10/3):
        self.t = [0]
        self.x, self.y, self.z = [1], [0], [0]
        self.r, self.sigma, self.b = _r, _sigma, _b
        self.dt, self.time, self.n = _dt, _time, int(_time/_dt)
        print 'Lorenz init, dt=%.3f, time=%.3f, r=%.3f '%(self.dt,self.time,self.r)
    def cal(self):           # use Euler method solves Lorenz Equations numerically
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)           
            self.x.append(self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-self.b*self.z[-1])*self.dt)
        print 'Lorenz cal',1
    def plot_z(self,_ax):           # plot trajectory z vs time
        _ax.plot(self.t,self.z,'-r',label='r= %.2f'%self.r)
        print 'z_t plot',1
    def plot_x(self,_ax):           # plot trajectory x vs time
        _ax.plot(self.t,self.x,'-r',label='r= %.2f'%self.r)
        print 'x_t plot',1
    def plot_y(self,_ax):           # plot trajectory y vs time
        _ax.plot(self.t,self.y,'-r',label='r= %.2f'%self.r)
        print 'y_t plot',1
    def plot_phase_zx(self,_ax):           # plot phase-space z vs x
        _ax.plot(self.x,self.z,'ob',markersize=0.3,label='r= %.2f'%self.r)
        print 'zx phase plot',1
    def plot_phase_xy(self,_ax):           # plot phase-space x vs y
        _ax.plot(self.y,self.x,'ob',markersize=0.3,label='r= %.2f'%self.r)
        print 'xy phase plot',1
    def plot_phase_yz(self,_ax):           # plot phase-space y vs z
        _ax.plot(self.z,self.y,'ob',markersize=0.3,label='r= %.2f'%self.r)
        print 'yz phase plot',1
    def plot_section_zx(self,_ax,_secy=0.):           # plot phase-space z vs x at y=0 section
        self.z_sec, self.x_sec = [], []
        self.secy = _secy
        for i in range(len(self.t)):
            if abs(self.y[i]-self.secy)<4E-3:
                self.z_sec.append(self.z[i])
                self.x_sec.append(self.x[i])
        if len(self.z_sec)>0:
            _ax.plot(self.x_sec,self.z_sec,'ok',markersize=4,label='r= %.2f'%self.r)
            print 'section plot,secy=',self.secy
            return 1
        else:
            print 'sec_y overranging'
            return 0


# plot phase space and section
fig= plt.figure(figsize=(10,10))
ax1=plt.axes([0.1,0.55,0.35,0.35])
ax2=plt.axes([0.6,0.55,0.35,0.35])
ax3=plt.axes([0.1,0.1,0.35,0.35])
ax4=plt.axes([0.6,0.1,0.35,0.35])

cmp=LORENZ(29.)
cmp.cal()
cmp.plot_phase_xy(ax1)
cmp.plot_phase_yz(ax2)
cmp.plot_phase_zx(ax3)
cmp=LORENZ(29.,0.001,1000)
cmp.cal()
cmp.plot_section_zx(ax4)

ax1.legend(loc='lower right')
ax2.legend(loc='lower right')
ax3.legend(loc='lower right')
ax4.legend(loc='lower right')
ax1.set_xlabel('y',fontsize=18)
ax2.set_xlabel('z',fontsize=18)
ax3.set_xlabel('x',fontsize=18)
ax4.set_xlabel('x',fontsize=18)
ax1.set_ylabel('x',fontsize=18)
ax2.set_ylabel('y',fontsize=18)
ax3.set_ylabel('z',fontsize=18)
ax4.set_ylabel('z',fontsize=18)
ax1.set_title('Phase space :x versus y',fontsize=18)
ax2.set_title('Phase space :y versus z',fontsize=18)
ax3.set_title('Phase space :z versus x',fontsize=18)
ax4.set_title('Section y=0 :z versus x',fontsize=18)

plt.show(fig)


            

