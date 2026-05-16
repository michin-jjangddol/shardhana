"""
core/state.py
상태 변수 구조

State variables for Shardhana elements

State represents time-dependent variables.
"""

class State:
    """
    Time-dependent state variables
    """

    def __init__(
        self,
        pressure: float = 0.0,
        temperature: float = 0.0,
        velocity: float = 0.0,
        acceleration: float = 0.0,
        moisture: float = 0.0,
    ):

        self.pressure = float(pressure)
        self.temperature = float(temperature)

        self.velocity = float(velocity)
        self.acceleration = float(acceleration)

        self.moisture = float(moisture)