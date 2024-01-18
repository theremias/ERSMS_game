from node import Node, Protection_possibility
from climbing_section import Climbing_section, Character
from climber import Climber


class Crag:
    """A class representing a climbing crag. Crag is a graph, it starts from Node APPROACH and ends in Node SUMMIT. 
        Apart from mentioned Nodes, there are several other Nodes, all are connected with Climbing_sections.
    """

    def __init__(self, sections_list: list[Climbing_section], approach_node: Node, summit_node: Node) -> None:
        """
        """
        self.sections_list = sections_list
        self.approach_node = approach_node
        self.summit_node = summit_node
        self.nodes_protected = [approach_node]

    def sections_above(self, current_node: Node) -> list[Climbing_section]:
        """Returns list of sections connected to 'current_node', wich are above the node.
        """
        result = []
        for section in self.sections_list:
            if section.from_node == current_node:
                result.append(section)
        return result
    
    def sections_below(self, current_node: Node) -> list[Climbing_section]:
        """Returns a list of sections connected to 'current_node', which are below the node.
        """
        result = []
        for section in self.sections_list:
            if section.to_node == current_node:
                result.append(section)
        return result

    def is_summited(self, current_node: Node) -> bool:
        """Returns True if a Climber reaches a SUMMIT Node, or False otherwise"""
        return current_node == self.summit_node
    
    def is_blind(self, current_node: Node) -> bool:
        """Returns True if there are NO Climbing_sections above current_node, or False otherwise"""
        next_sec = self.sections_above(current_node)
        return len(next_sec) == 0
    
    def use_protection(self, current_node: Node) -> None:
        """Appends a Node where climber used protection to the list of protected Nodes at current Crag"""
        self.nodes_protected.append(current_node)
        current_node.use_protection()
        text = "\nYou used {} in Node {}\n".format(current_node.protection_possibility, current_node)
        print(text)

    """def climb_section(self, section: Climbing_section, climber: Climber) -> None:
        if climber.attempt_climb(section):
            section.change_is_climbed()
            self.used_protections.append"""
    
    def __str__(self) -> str:
        num_sections = len(self.sections_list)
        result = "You are on {} crag. There are {} climbing sections.".format(self.approach_node, num_sections)
        return result
        
def main():
    bot1 = Node("BOT1")
    cra1 = Node("CRA1", Protection_possibility.BOLT)
    cra2 = Node("CRA2", Protection_possibility.HOURGLASS)
    cra3 = Node("CRA3", Protection_possibility.CRACK)
    top1 = Node("TOP1", Protection_possibility.RING)
    bli1 = Node("BLI1", Protection_possibility.NOTHING)
    sid1 = Node("SID1", Protection_possibility.CRACK)

    sec1 = Climbing_section(bot1, cra1)
    sec2 = Climbing_section(cra1, cra2, str_diff=2, character=Character.CRIMPS) 
    sec3 = Climbing_section(cra2, cra3, character=Character.CRIMPS)
    sec4 = Climbing_section(cra3, top1)
    sec5 = Climbing_section(cra1, bli1)
    sec6 = Climbing_section(cra2, sid1)
    sec7 = Climbing_section(sid1, cra3)

    route_list = [sec1, sec2, sec3, sec4, sec5, sec6, sec7]

    my_route = Crag(route_list, bot1, top1)
    print(my_route)
    for node in [bot1, cra1]:
        print("Using node: {}".format(node))
        next_sections = my_route.sections_above(node)
        
        print(next_sections)



if __name__ == "__main__":
    main()      