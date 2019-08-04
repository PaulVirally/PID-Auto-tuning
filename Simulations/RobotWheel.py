import random
from Utils import remap
from .Simulator import Simulator

class RobotWheel(Simulator):
    """Simulates a wheel (or pair of wheels) on a robot that respond to a certain voltage (ranging from -1 to 1)."""

    def __init__(self, responsiveness=10.0, entropy=0.05, friction=0.5):
        """Constructs a RobotWheel.
        
        Arguments:
            responsiveness {float}: How responsive the RobotWheel is to voltage (the higher, the more responsive)
            entropy {float}: Ranges from 0 to 1. The maximum probability the voltage can vary from what the user sets it to.
            friction {float}: A coefficient of friction (where the friction is proportional to the veloctity squared for this Simulator)
        """
        self._pos = 0.0
        self._velo = 0.0
        self._voltage = 0.0
        self._responsiveness = responsiveness
        self._entropy = entropy
        self._friction = friction

    def set_input(self, val: float) -> float:
        """Set the voltage to the wheels of the RobotWheel.

        Arguments:
            val {float} -- The voltage of the wheel (ranges from -1 to 1 for simplicity)
        """
        # Add in a bit of randomness to the system
        self._voltage = val * (1.0 - random.uniform(-self._entropy, self._entropy))

    def _get_force(self) -> float:
        """Converts the voltage set on the wheel to a translational force applied on RobotWheel body.

        Returns:
            float -- The force applied on the RobotWheel body.
        """
        # Arbitrary deadband value
        if abs(self._voltage) < 0.1:
            return 0.0

        if self._voltage > 0:
            voltage = remap(self._voltage, 0.1, 1.0, 0.0, 1.0)
        else:
            voltage = remap(self._voltage, -1.0, -0.1, -1.0, 0.0)

        # Arbitratry function for conversion between voltage and orce
        force = (voltage*self._responsiveness)**3

        # Arbitrary function for friction
        force -= self._friction * self._velo**2
        return force

    def get_output(self) -> float:
        """Get the position of the RobotWheel.
        
        Returns:
            float -- The position of the RobotWheel.
        """
        return self._pos

    def step(self, dt: float):
        """Takes a step in time for the RobotWheel.

        Arguments:
            dt {float} -- The small step in time.
        """
        force = self._get_force()

        dv = force * dt
        self._velo += dv

        dx = (2*self._velo - dv)/2 * dt
        self._pos += dx