from climbing_section import Climbing_section, Character

class Climber:
    """Climbing character.
    """

    def __init__(self) -> None:
        self.name = "Pepe"
        self.strength = 1
        self.technique = 1
        self.protection = 1
        self.is_alive = True
        self.exp_str = 0
        self.exp_tech = 0
        self.exp_prot = 0

    def __str__(self) -> str:
        result = "Character {} is alive: {}\n".format(self.name, self.is_alive)
        result += "It's abilities are:\n"
        result += "  strength:   {} (exp: {})\n  technique:  {} (exp: {})\n  protection: {} (exp: {})".format(self.strength, self.exp_str, self.technique, self.exp_tech, self.protection, self.exp_prot)
        return result
    
    """def experiences(self) -> None:
        self.strngth = 0
        self.tchnq = 0
        self.prtctn = 0"""
    
    def gain_exp(self, exp_str: int=0, exp_tech: int=0, exp_prot: int=0) -> None:
        self.exp_str += exp_str
        self.exp_tech += exp_tech
        self.exp_prot += exp_prot

    def determine_experience(self, ability: int, challenge: int) -> int:
        result = 0
        test = challenge - ability
        result = int(1.5**(test)*10)
        return result

    def gain_level(self) -> None:
        """If a Climber meets the criteria to gain a new level in their abilities, one level of ability is gained and
            corresponding (to criteria) experiences are lost."""
        # abilities = [self.strength, self.technique, self.protection]
        # experiences = [self.exp_str, self.exp_tech, self.exp_prot]
        fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        str_limit  = 100 * fibonacci[self.strength - 1]
        tech_limit = 100 * fibonacci[self.technique - 1]
        prot_limit = 100 * fibonacci[self.protection - 1]
        if self.exp_str >= str_limit:
            self.strength += 1
            self.exp_str -= str_limit
        if self.exp_tech >= tech_limit:
            self.technique += 1
            self.exp_tech -= tech_limit
        if self.exp_prot >= prot_limit:
            self.protection +=1
            self.exp_prot -= prot_limit
        # for ab in abilities:
        #     limit = 100 * fibonacci[ab - 1]
        #     for exp in experiences:
        #         while exp >= limit:
        #             self += ab
                    

    """def abilities(self):
        self.strength = 1
        self.technique = 1
        self.protection = 1"""

    def set_abilities(self, strength: int, technique: int, protection: int) -> None:
        """Sets a Climbers abilities."""
        self.strength = strength
        self.technique = technique
        self.protection = protection

    def can_climb(self, climbing_section: Climbing_section) -> bool:
        """Returns True if climber is able to climb a section, False if is NOT able.
        """
        if climbing_section.str_difficulty <= self.strength and climbing_section.tech_difficulty <= self.technique: 
            return True
        else:
            return False
        
    def die(self) -> None:
        """Sets 'self.is_alive' to False."""
        self.is_alive = False

def main():
    player = Climber()
    print(player)
    player.set_abilities(2, 3, 2)
    player.die()
    new_exp = player.determine_experience(player.strength, 8)
    player.gain_exp(exp_prot=new_exp)
    print(player)
    player.gain_level()
    print(player)

    
if __name__ == "__main__":
    main()