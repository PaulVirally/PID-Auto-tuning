from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from Simulations import Simulator
from PIDController import PIDController

def _get_mse(controller: PIDController, num_pts: float, dt: float) -> float:
    """Returns the mean squared error of the PIDController.
    
    Arguments:
        controller {PIDController} -- The PIDController to use.
        num_pts {float} -- The number of points to use for the PIDController.
        dt {float} -- The time step for the PIDController.
    
    Returns:
        float -- The root squared error of the PIDController.
    """
    mse = 0
    for _ in range(num_pts):
        controller.step(dt)
        err = controller.get_error()
        mse += err**2
    mse /= num_pts
    return mse

class PIDTuner:

    def __init__(self, sim: Simulator, setpoint: float, t0: float, t1: float, dt: float):
        """Constructs a PIDTuner.
        
        Arguments:
            sim {Simulator} -- The Simulator to use for the PIDTuner.
            setpoint {float} -- The setpoint for the PIDTuner.
            t0 {float} -- The initial time to start the simulation at.
            t1 {float} -- The final time to end the simulation at.
            dt {float} -- The incremental time step in each simulation. 
        """
        self._sim = sim
        self._setpoint = setpoint

        self._dt = dt
        num_pts = (t1-t0)/dt
        self._ts = np.linspace(t0, t1, num=num_pts)

        self._controller = PIDController(sim, setpoint, 1, 1, 1) # TODO: Optimize initial PID values

        self._prev_grad = ()
        self._prev_vals = ()

    def _get_gradient(self, delta=0.01) -> (float, float, float):
        """Returns the gradient of the mean squared error of the Simulation with respect to each kp, ki, and kd value.
        
        Arguments:
            delta {float} -- The small change in each kp, ki, and kd value.
        
        Returns:
            (float, float, float) -- The gradient of the mean squared error of the Simulation with respect to each kp, ki, and kd value.
        """
        mse_before = _get_mse(deepcopy(self._controller), len(self._ts), self._dt)

        dp_controller = PIDController(deepcopy(self._sim), self._setpoint, self._controller.kp + delta, self._controller.ki, self._controller.kd)
        dp = _get_mse(dp_controller, len(self._ts), self._dt) - mse_before

        di_controller = PIDController(deepcopy(self._sim), self._setpoint, self._controller.kp, self._controller.ki + delta, self._controller.kd)
        di = _get_mse(di_controller, len(self._ts), self._dt) - mse_before

        dd_controller = PIDController(deepcopy(self._sim), self._setpoint, self._controller.kp, self._controller.ki, self._controller.kd + delta)
        dd = _get_mse(dd_controller, len(self._ts), self._dt) - mse_before

        return (dp/delta, di/delta, dd/delta)

    def epoch(self):
        """Takes one step in tuning the kp, ki, and kd values.
        """
        old_vals = (self._controller.kp, self._controller.ki, self._controller.kd)
        gamma = 0.1
        grad = self._get_gradient()

        new_vals = [p - gamma*g for p, g in zip(old_vals, grad)]

        self._controller.kp = new_vals[0] if new_vals[0] > 0 else 0
        self._controller.ki = new_vals[1] if new_vals[1] > 0 else 0
        self._controller.kd = new_vals[2] if new_vals[2] > 0 else 0

    def get_vals(self) -> (float, float, float):
        """Returns the computed, kp, ki, and kd values.
        
        Returns:
            (float, float, float) -- The kp, ki, and kd values.
        """
        return (self._controller.kp, self._controller.ki, self._controller.kd)

    def get_controller(self) -> PIDController:
        """Returns the tuned PIDController.
        
        Returns:
            PIDController -- The tunend PIDController.
        """
        return deepcopy(self._controller)

    def plot_curve(self):
        """Plots the PID curve for the tuned PIDController using matplotlib. You still need to call plt.show() to see the actual curve.
        """
        controller = deepcopy(self._controller)
        data = np.zeros(len(self._ts))
        for i in range(len(self._ts)):
            controller.step(self._dt)
            data[i] = controller.sim.get_output()
        plt.plot(self._ts, data)
        plt.plot(self._ts, [self._setpoint]*len(self._ts))