from Simulations import Simulator

class PIDController:
    """Controller for a system using a PID loop."""

    def __init__(self, sim: Simulator, setpoint: float, kp: float, ki: float, kd: float):
        """Constructs a PIDController.

        Arguments:
            sim {Simulator} -- The Simulator the controller will use.
            setpoint {float} -- The target value the Simulator must reach.
            kp {float} -- Proportional constant in PID.
            ki {float} -- Integral constant in PID.
            kd {float} -- Derivative connstant in PID.
        """
        self.sim = sim
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self._previous_value = 0 # Used for the derivative term
        self._integral = 0 # Used for the integral term

    def get_error(self) -> float:
        return self.setpoint - self.sim.get_output()

    def _get_input(self, dt: float) -> float:
        """Computes the P, I, and D terms to get the input that should be given to the simulated system.
        
        Arguments:
            dt {float} -- The time interval between time steps.

        Returns:
            float -- The input that should be given to the system.
        """
        err = self.get_error()

        p = self.kp * err

        self._integral += err * dt
        i = self.ki * self._integral

        d = self.kd * (self.sim.get_output() - self._previous_value)/dt

        return p + i + d

    def step(self, dt: float):
        """Takes a step in time for the PIDController.

        The P, I, and D terms are calculated to find the new input to give to the system.
        The simulated system is then updated according to the computed input.
        
        Arguments:
            dt {float} -- [description]
        """
        inpt = self._get_input(dt)
        self.sim.set_input(inpt)
        self._previous_value = self.sim.get_output()
        self.sim.step(dt)