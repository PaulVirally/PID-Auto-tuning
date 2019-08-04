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

def clamp(x: float, min_x: float, max_x: float) -> float:
    """Clamps `x` to `min_x` on the bottom and `max_x` on the top.
    
    Arguments:
        x {float} -- The value to clamp.
        min_x {float} -- The floor of the clamp.
        max_x {float} -- The ceiling of the clamp.
    
    Returns:
        float -- The new clamped value.
    """
    if x < min_x:
        return min_x
    elif x > max_x:
        return max_x
    return x

def signum(x: float) -> float:
    """Returns the sign of `x`.
    
    Arguments:
        x {float} -- The value to be tested.
    
    Returns:
        float -- Returns +1.0 if `x` > 0, -1.0 if `x` < 0, and 0.0 if `x` == 0.
    """
    if x < 0:
        return -1.0
    elif x > 0:
        return 1.0
    return 0.0