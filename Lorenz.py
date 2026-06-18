import numpy as np
import matplotlib.pyplot as plt

def calc():
    sigma = 10.
    b = 8/3
    r = 28
    dt = 0.01
    i = 0
    tmax = 50
    n = int(tmax/dt)

    data = np.zeros((n, 3))
    x, y, z = 1.0, 1.0, 1.0
    
    filename = f"calc.dat"

    for i in range(n):
        x = (1-sigma*dt)*x + sigma*dt*y
        y = (y+dt*x*(r-z))/(1+dt)
        z = (z+x*y*dt)/(1+b*dt)
        data[i] = [x, y, z]
    np.savetxt(filename, data)
    return filename

def draw_2d(path, col_x, col_y, xlabel, ylabel):

    data = np.loadtxt(path)
    x_val = data[:, col_x]
    y_val = data[:, col_y]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1,1,1)
    
    label_text = (r"$\dot{\tilde{x}} = \sigma(y-x)$" + "\n" +
                  r"$\dot{\tilde{y}} = rx-y-xz$" + "\n" +
                  r"$\dot{\tilde{z}} = xy-bz(numerical)$")
    plt.plot(x_val, y_val, "-", color="b", lw=0.5, label=label_text)
    ax.set_xlabel(xlabel, size=20)
    ax.set_ylabel(ylabel, size=20)
    ax.legend(fontsize=15)
    ax.set_title("Lorenz Attractor", fontsize=15)
    ax.grid(True, linestyle="--", alpha=0.7)
    for spine in ax.spines.values():
        spine.set_linewidth(2)

    plt.savefig(f"./lorenz_{xlabel}_{ylabel}.pdf")
    plt.close()

def draw_3d(path):
    data = np.loadtxt(path)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    label_text = (r"$\dot{\tilde{x}} = \sigma(y-x)$" + "\n" +
                  r"$\dot{\tilde{y}} = rx-y-xz$" + "\n" +
                  r"$\dot{\tilde{z}} = xy-bz(numerical)$")
    ax.plot(data[:,0], data[:,1], data[:,2], lw=0.5, label= label_text)
    ax.legend(fontsize=15)
    ax.set_title("Lorenz Attractor", fontsize=15)
    ax.grid(True, linestyle="--", alpha=0.7)
    for spine in ax.spines.values():
        spine.set_linewidth(2)
        
    plt.savefig("lorenz_3D.pdf")
    plt.close()
#====================
#       実行
#====================
filename = calc()
draw_2d(filename, 0, 1, "x", "y")
draw_2d(filename, 1, 2, "y", "z")
draw_3d(filename)