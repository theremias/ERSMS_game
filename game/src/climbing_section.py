from enum import Enum
from node import Node, Protection_possibility


class Character (Enum):
    SLAB = 0
    VERTICAL = 1
    OVERHANG = 2
    
    CRACK = 3
    CRIMPS = 4
    CHIMNEY = 5
    

class Climbing_section:
    """A climbing section between nodes.
    """

    def __init__(self, start_node: Node, end_node: Node , str_diff: int = 1, tech_diff: int = 1, character: Character = Character.VERTICAL ) -> None:
        self.from_node: Node = start_node
        self.to_node: Node = end_node
        self.str_difficulty: int = str_diff
        self.tech_difficulty: int = tech_diff
        self.character: Character = character
        # whether the section was climbed in current session (its important, because you can only return the way you climbed up)
        self.is_climbed = False
        

    
    def __repr__(self) -> str:
        return "section from node {} to node {}, (str: {}, tech: {}, char: {}).".format(self.from_node, self.to_node, self.str_difficulty, self.tech_difficulty, self.character)
    
    def start_node(self):
        pass

    def end_node(self):
        pass
    
    

def main():
    node1 = Node("A1")
    node2 = Node("A2", Protection_possibility.RING)
    u = Climbing_section(node1, node2)
    # u.tech_difficulty = 10 <== NEDELEJ!
    print(u)

    u2 = Climbing_section(node1,node2,tech_diff = 5, str_diff = 8)
    for c in Character:
        u2.character = c
        print(u2)

if __name__ == "__main__":
    main()