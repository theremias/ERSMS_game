from random import random

from climbing_section import Climbing_section, Character
from node import Node, Protection_possibility

class Climber:
    """Climbing character.
    """

    def __init__(self) -> None:
        self.name = "Pepe"
        self.is_alive = True
        self.experiences = {"strength": 0, "technique": 0, "protection": 0}
    
    def get_strength(self) -> int:
        return self._get_ability("strength")

    def get_technique(self) -> int:
        return self._get_ability("technique")
    
    def get_protection(self) -> int:
        return self._get_ability("protection")
    
    def gain_exp_section(self, section: Climbing_section) -> None:
        self.experiences["strength"] += self._determine_experience(self.get_strength(), section.str_difficulty)
        self.experiences["technique"] += self._determine_experience(self.get_technique(), section.tech_difficulty)

    def attempt_climb(self, climbing_section: Climbing_section) -> bool:
        """Returns True if climber is able to climb a section, False if is NOT able.
        """
        tst = random()
        str_test = self._get_probability(self.get_strength(), climbing_section.str_difficulty) > tst
        tech_test = self._get_probability(self.get_technique(), climbing_section.tech_difficulty) > tst
        return str_test and tech_test
        
    def die(self) -> None:
        """Sets 'self.is_alive' to False."""
        self.is_alive = False
    
    def _determine_experience(self, ability: int, challenge: int) -> int:
        result = 0
        test = challenge - ability
        result = int((1.5**test) *10)
        return result
           
    def _get_ability(self, ability: str) -> int:
        """TODO: komentar"""
        result = 0
        fibonacci = [x*100 for x in [1, 1, 2, 3, 5, 8, 13, 21, 34]]
        exp = self.experiences[ability]
        for i in fibonacci:
            if exp >= i:
                result += 1
                exp -= i
            else:
                break
        return result

    def _get_probability(self, ability: int, test: int) -> float:
        variable = ability - test
        if variable > 3:
            return 1.00
        elif variable < -7:
            return 0.00
        return (variable + 7)/10

    def __str__(self) -> str:
        result = "Character {} is {}\n".format(self.name, "alive" if self.is_alive else "dead")
        result += "It's abilities are:\n"
        result += "  strength:   {} (exp: {})\n".format(self.get_strength(), self.experiences["strength"])
        result += "  technique:  {} (exp: {})\n".format(self.get_technique(), self.experiences["technique"])
        result += "  protection: {} (exp: {})".format(self.get_protection(), self.experiences["protection"])
        return result

def main():
    player = Climber()
    node1 = Node("node 1", Protection_possibility.BOLT)
    node2 = Node("node 2", Protection_possibility.RING)
    section = Climbing_section(node1, node2, 0, 1, Character.CRACK)
    print(player)
    player.die()
    player.gain_exp_section(section)
    print(player)

    
if __name__ == "__main__":
    main()