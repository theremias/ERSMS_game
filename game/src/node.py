from enum import Enum

class Protection_possibility (Enum):
    BOLT = 1

    RING = 3
    CRACK = 4
    HOURGLASS = 5
    NOTHING = 0

class Node:
    """A node in the climbing route. Nodes are connected with Climbing_sections.
    """

    def __init__(self, name: str, protection: Protection_possibility = Protection_possibility.NOTHING) -> None:
        self.name = name
        self.protection_possibility = protection

    def __str__(self) -> str:
        return "{}, here you can use {}".format(self.name, self.protection_possibility)
    
    def __repr__(self) -> str:
        return self.__str__()
    
