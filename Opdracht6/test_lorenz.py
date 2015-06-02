import sys
sys.path.append('/home/ubuntu/workspace/pip')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages

from lorenz import *

L1=Lorenz([-1,1,0])
u1=L1.solve(50,0.01)
L2=Lorenz([-1.001,1.001,0.001])
u2=L2.solve(50,0.01)

print(u1[0][0], u2[0][0])
print(u1[-1][0], u2[-1][0])

with PdfPages('plot.pdf') as pdf:
    transpose = list(map(list, zip(*u1)))
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(transpose[0], transpose[1], transpose[2]) # transpose2 en dan komt een andere plot in dezelfde figuur
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    pdf.savefig() 



