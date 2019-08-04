def remap(x: float, min_x: float, max_x: float, min_y: float, max_y: float) -> float:
    """Remaps the value `x` (ranging from `min_x` to `max_x`) to a value ranging from `min_y` to `max_y`.

    Arguments:
        x {float}: The input value to be remapped.
        min_x {float} -- The minimum value `x` can take on.
        min_x {float} -- The maximum value `x` can take on.
        min_y {float} -- The minimum value the output can take on.
        min_y {float} -- The maximum value the output can take on.

    Returns:
        float: The remapped value ranging from `min_y` to `max_y`.
    """
    return min_y + (max_y - min_y) * ((x - min_x) / (max_x - min_x))