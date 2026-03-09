# src/shardhana/state.py

"""
State variables of an element
"""


class State:
    """
    Time-dependent state variables
    """

    def __init__(self):

        self.pressure = 0.0
        self.temperature = 0.0

        self.velocity = 0.0
        self.acceleration = 0.0

        self.moisture = 0.0