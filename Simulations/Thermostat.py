import random
from Utils import clamp
from .Simulator import Simulator

class Thermostat(Simulator):
    """Simulates a thermostat."""

    def __init__(self, initial_temp=20.0, ambient_temp=20.0, heater_temp=35.0, heat_coefficient=1.0, entropy=0.2):
        """Constructs a Thermostat.

        Arguments:
            initial_temp {float} -- The initial temperature of the room.
            ambient_temp {float} -- The ambient temperature of the room.
            heater_temp {float} -- The temperature of the heating unit.
            heat_coefficient {float} -- How easily the air can be heated by the heather.
            entropy {float} -- Ranges from 0 to 1. The maximum probability the air flow can vary from what the user sets it to.
        """
        super().__init__(0.0, 1.0)
        self._temp = initial_temp
        self._ambient_temp = ambient_temp
        self._heater_temp = heater_temp
        self._heat_coefficient = heat_coefficient
        self._entropy = entropy
        self._flow = 0.0

    def set_input(self, flow: float) -> float:
        """Turns on the heating unit by a certain amount.

        Arguments:
            flow {float} -- The percentage (0 to 1) flow of hot air coming out of the heating unit.
        """
        self._flow = clamp(flow, 0.0, 1.0)

    def get_output(self) -> float:
        """Get the temperature measured by the Thermostat.
        
        Returns:
            float -- The temperature of the room.
        """
        return self._temp

    def step(self, dt: float):
        """Takes a step in time for the Thermostat.

        Arguments:
            dt {float} -- The small step in time.
        """
        hot_delta_temp = self._flow * self._heat_coefficient * (self._heater_temp - self._temp)
        ambient_delta_temp = self._heat_coefficient * (self._ambient_temp - self._temp)
        delta_temp = hot_delta_temp + ambient_delta_temp
        entropy = random.uniform(-self._entropy, self._entropy)
        delta_temp += entropy * delta_temp
        self._temp += delta_temp * dt