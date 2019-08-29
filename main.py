from datetime import datetime
import matplotlib.pyplot as plt
from Simulations.RobotWheel import RobotWheel
from Simulations.Thermostat import Thermostat
from PIDTuner import PIDTuner

num_epochs = 100
fig = plt.figure()

thermostat_setpoint = 25
thermostat_sim = Thermostat(entropy=0.0)
thermostat_tuner = PIDTuner(thermostat_sim, thermostat_setpoint, t0=0, t1=3, dt=0.001)
thermostat_ax = fig.add_subplot(211)

wheel_setpoint = 3
wheel_sim = RobotWheel(entropy=0.0)
wheel_tuner = PIDTuner(wheel_sim, wheel_setpoint, t0=0, t1=50, dt=0.01)
wheel_ax = fig.add_subplot(212)

print('Tuning...')
start_time = datetime.now()
for i in range(num_epochs):
    if i == 5:
        thermostat_tuner.plot_curve(label=f'{i} Epoch' + ('s' if i != 1 else ''), axis=thermostat_ax)
        wheel_tuner.plot_curve(label=f'{i} Epoch' + ('s' if i != 1 else ''), axis=wheel_ax)

    thermostat_tuner.epoch()
    wheel_tuner.epoch()

print(f'Time taken for {num_epochs} epochs: {datetime.now() - start_time}')
print(f'Thermostat PID Values: {thermostat_tuner.get_vals()}')
print(f'RobotWheel PID Values: {wheel_tuner.get_vals()}')

thermostat_tuner.plot_curve(f'{num_epochs} Epochs', axis=thermostat_ax)
thermostat_ax.plot(thermostat_tuner._ts, [thermostat_tuner._setpoint]*len(thermostat_tuner._ts), label='Setpoint')

wheel_tuner.plot_curve(f'{num_epochs} Epochs', axis=wheel_ax)
wheel_ax.plot(wheel_tuner._ts, [wheel_tuner._setpoint]*len(wheel_tuner._ts), label='Setpoint')

thermostat_ax.legend()
wheel_ax.legend()

thermostat_ax.set_title('Temperature over time')
# thermostat_ax.set_xlabel('Time (arb.)')
thermostat_ax.set_ylabel('Temperature (arb.)')

wheel_ax.set_title('Wheel distance over time')
wheel_ax.set_xlabel('Time (arb.)')
wheel_ax.set_ylabel('Distance (arb.)')

plt.show()