import sys

from crag import Crag
from climber import Climber
from node import Node, Protection_possibility
from climbing_section import Climbing_section, Character
from map import create_map



class Game:
    """Class representing a game about climbing.
    """

    def __init__(self) -> None:
        self.show_help()
        chosen_name = input("Choose a name: ")
        self.climber = Climber(name = chosen_name)
        self.crag = create_map()
        self.position = self.crag.approach_node
        self.is_quitted = False

    def is_won(self) -> bool:
        return self.crag.is_summited(self.position)

    def is_lost(self) -> bool:
        return not self.climber.is_alive or ( self.crag.is_blind(self.position) and not self.is_won() )

    def is_finished(self) -> bool:
        return self.is_won() or self.is_lost()
    
    def show_help(self) -> None:
        result = ""
        header = "\n=== === === === === === HELP for game ERSMS === === === === === ===\n"

        row1_0 = "You are playing a game about climbing called ERSMS. The game is controlled via terminal.\n"
        row2_0 = "You can type several commands to progress in the game:\n"
        row3_0 = " 0, 1, ...   for route options\n"
        row3_1 = " p           to try to use a protection\n"
        row4_0 = " h           to access help\n"
        row5_0 = " i           to access character info\n"
        row6_0 = " q           to quit the game\n"
        row7_0 = " r           to restart the game\n\n"
        text = row1_0 + row2_0 + row3_0 + row3_1 + row4_0 + row5_0 + row6_0 + row7_0

        result = header + text
        print(result)

    def show_info(self) -> None:
        result = ""
        header = "\n=== === === === === === CHARACTER INFO === === === === === ===\n"

        text = "Your character is named {}. Its strength is {} ({}) and technique {} ({})\n\n".format(self.climber.name, 
                                                                                          self.climber.get_strength(), self.climber.experiences["strength"], 
                                                                                          self.climber.get_technique(), self.climber.experiences["technique"])
        result = header + text
        print(result)

    def run(self) -> bool:
        """Returns True while the Game should be restarted, False otherwise."""
        while True:
            if self.is_finished():
                break
            print("You are in node:", repr(self.position))
            next_sections = self.crag.sections_above(self.position)
            num_next_sec = len(next_sections)

            """if not (self.position.protection_possibility == Protection_possibility.NOTHING) and not self.position.protection_used:
                while True:
                    player_input = input("Do you wish use a protection? (y/n)")
                    if player_input == "y":
                        self.crag.use_protection(self.position)
                        break
                    elif player_input == "n":
                        break
                    else:
                        print("Invalid input")
                        continue """

            
            
            while True:
                print("You can climb:")
                for i in range(num_next_sec):
                    print(i, next_sections[i])
                player_input = input("Choose your next action: ")
                if player_input == "p":
                    if not (self.position.protection_possibility == Protection_possibility.NOTHING):
                        self.crag.use_protection(self.position)
                    continue
                if player_input == "h":
                    self.show_help()
                    continue
                if player_input == "i":
                    self.show_info()
                    continue
                if player_input == "q":
                    print("Quitting the game...")
                    return False
                if player_input == "r":
                    print("Restarting the game...")
                    return True
                
                try:
                    choice = int(player_input)
                except:
                    print("Invalid input")
                    continue

                if not (0 <= choice < num_next_sec):
                    print("Number too big (or negative)")
                    continue

                break
            
            chosen_section = next_sections[choice]
            lastNode_prot_used = self.crag.nodes_protected[-1]

            if self.climber.attempt_climb(chosen_section):
                print("\nYou succefully climbed the section.\n")
                self.position = chosen_section.to_node
                self.climber.gain_exp_section(chosen_section)
                chosen_section.change_is_climbed()
                """elif lastNode_prot_used == self.position: 
                print("You failed to climb a section and now you're back at the begining of the section.")"""
            elif self.position.heigth - lastNode_prot_used.heigth < 5:
                self.position = lastNode_prot_used
                print("You failed to climb a section and falled back to the last protection used")
            else:
                self.climber.die()
                print("You failed to climb a section and died while falling.")
                # TODO: spadl a umrel > konec hry

        if self.is_won():
            print("VICTORY!")
        elif self.is_lost():
            print("Try again")

            
def main():
    running = True
    while running:
        game = Game()
        running = game.run()

if __name__ == "__main__":
    main()      