

class Inventory:
    """A class representing a climbers inventory.
    """

    def __init__(self) -> None:
        self.carabiners = 0
        self.slings = 0

    def gain_carabiners(self, number: int) -> None:
        self.carabiners += number

    def gain_slings(self, number: int) -> None:
        self.slings += number