from enum import Enum
from node import Node


class Character (Enum):
    SLAB = 0
    VERITCAL = 1
    OVERHANG = 2
    
    FINGER_CRACK = 3
    HANDJAM = 4
    FISTJAM = 5
    CHICKENWING = 6
    CHIMNEY = 7

class Climbing_section:
    """A climbing section between nodes.
    """

    def __init__(self, start_node: Node, end_node: Node , str_diff: int = 1, tech_diff: int = 1, character: Character = Character.VERITCAL ) -> None:
        self.from_node: Node = start_node
        self.to_node: Node = end_node
        self.str_difficulty: int = str_diff
        self.tech_difficulty: int = tech_diff
        self.character: Character = character
        # whether the section was climbed in current session (its important, because you can only return the way you climbed up)
        self.is_climbed = False
        
    
    def __str__(self) -> str:
        return "Usek: {} (sila = {}, tech. nar. = {}), z uzlu {} do uzlu {}.".format(self.character, self.str_difficulty, self.tech_difficulty, self.from_node, self.to_node)
    
    def start_node(self):
        pass

    def end_node(self):
        pass
    

def main():
    u = Climbing_section(5, 1)
    # u.tech_difficulty = 10 <== NEDELEJ!
    print(u)

    u2 = Climbing_section(1,1,tech_diff = 5, str_diff = 8)
    for c in Character:
        u2.character = c
        print(u2)

if __name__ == "__main__":
    main()