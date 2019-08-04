class PIDController:
    """Controller for a system using a PID loop."""

    def __init__(self, kp: float, ki: float, kd: float):
        """Constructs the PIDController

        Arguments:
            kp {float} -- Proportional constant in PID
            ki {float} -- Integral constant in PID
            kd {float} -- Derivative connstant in PID
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def my_func(self, a: float, b: float) -> float:
        """[summary]
        
        Arguments:
            a {float} -- [description]
            b {float} -- [description]
        
        Returns:
            float -- [description]
        """
        return a * self.kp + b