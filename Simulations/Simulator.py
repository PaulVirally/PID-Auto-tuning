class Simulator:
    """Abstract class for all simulations to provide a consistent API."""

    def set_input(self, val):
        """Set the input to the Simulator.

        Arguments:
            val -- The value the Simulator takes in as its input.
        """
        raise NotImplementedError

    def get_output(self):
        """Get the output of the Simulator (the measurement used for the PID loop)."""
        raise NotImplementedError

    def step(self, dt: float):
        """Takes a step in time for the Simulator.

        Arguments:
            dt {float} -- The small step in time.
        """
        raise NotImplementedError