# src/shardhana/element.py

"""
Shardhana Element definition

Basic concept

Element = Node + Seed + Space + State + Relations

Node      : Represents the position of an element.
Seed      : Material core of the element
Space     : Surrounding interaction space
State     : Time-dependent variables
Relations : Dynamic relationship between neighboring elements
"""

from .node import Node
from .material import Material
from .state import State


class Seed:
    """
    Structural core of the element
    """

    def __init__(self, shape=None):

        self.material = Material()
        self.volume = 0.0
        self.shape = shape


class Space:
    """
    Space surrounding the seed
    """

    def __init__(self, density=0.0, volume=0.0, shape=None):

        self.density = density
        self.volume = volume
        self.shape = shape


class Relation:
    """
    Relation between elements.

    Represents the spatial and physical relationship
    between two neighboring elements.

    Relations may include relative position, distance,
    contact state, or connection state.

    Unlike FEM connectivity, relations are not fixed
    and may change over time.
    """

    def __init__(self):

        self.target = None
        self.relative_vector = None
        self.distance = 0.0

        self.connected = False
        self.contact = False


class Element:
    """
    Basic HEM element

    Element = Node + Seed + Space + State + Relations
    """

    def __init__(self):

        self.node = Node()
        self.seed = Seed()
        self.space = Space()
        self.state = State()

        self.relations = []