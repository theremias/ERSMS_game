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

    def __init__(self, name: str, heigth: int, protection: Protection_possibility = Protection_possibility.NOTHING) -> None:
        self.name = name
        self.protection_possibility = protection
        self.protection_used = False
        self.heigth = heigth

    def use_protection(self) -> None:
        self.protection_used = True

    def change_height(self, new_height: int) -> None:
        self.heigth = new_height

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return "{}, here you can use {}\n".format(self.name, self.protection_possibility)
    
