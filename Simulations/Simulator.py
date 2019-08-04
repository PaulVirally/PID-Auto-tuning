class Simulator:
    """Abstract class for all simulations to provide a consistent API."""

    def __init__(self, min_input: float, max_input: float):
        """Constructs a Simulator with inputs varyinng between `min_input` and `max_input`.
        
        Arguments:
            min_input {float} -- The minimum value the Simulator can take in as an input.
            max_input {float} -- The maximum value the Simulator can take in as an input.
        """
        self.min_input = min_input
        self.max_input = max_input

    def set_input(self, val: float):
        """Set the input to the Simulator.

        Arguments:
            val {float} -- The value the Simulator takes in as its input.
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