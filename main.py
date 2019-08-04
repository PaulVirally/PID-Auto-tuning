import matplotlib.pyplot as plt
import numpy as np
from Simulations.RobotWheel import RobotWheel

rw = RobotWheel(entropy=0.2)

num_pts = 100
ts, dt = np.linspace(0, 10, num=num_pts, retstep=True)
xs = np.zeros(num_pts)
for i in range(num_pts):
    rw.set_input(0.5)
    rw.step(dt)
    rw[i] = rw.get_output()

plt.plot(ts, xs)
plt.show()