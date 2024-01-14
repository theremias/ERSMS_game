import sys

from route import Crag
from climber import Climber
from node import Node, Protection_possibility
from climbing_section import Climbing_section, Character



class Game:
    """Class representing a game about climbing.
    """

    def __init__(self) -> None:
        self.climber = Climber()

        bot1 = Node("BOT1")
        cra1 = Node("CRA1", Protection_possibility.BOLT)
        cra1.change_height(2)
        cra2 = Node("CRA2", Protection_possibility.HOURGLASS)
        cra2.change_height(5)
        cra3 = Node("CRA3", Protection_possibility.CRACK)
        cra3.change_height(7)
        top1 = Node("TOP1", Protection_possibility.RING)
        top1.change_height(12)
        bli1 = Node("BLI1", Protection_possibility.NOTHING)
        bli1.change_height(6)
        sid1 = Node("SID1", Protection_possibility.CRACK)
        sid1.change_height(6)

        sec1 = Climbing_section(bot1, cra1)
        sec2 = Climbing_section(cra1, cra2, str_diff=2, character=Character.CRIMPS) 
        sec3 = Climbing_section(cra2, cra3, character=Character.CRIMPS)
        sec4 = Climbing_section(cra3, top1)
        sec5 = Climbing_section(cra1, bli1)
        sec6 = Climbing_section(cra2, sid1)
        sec7 = Climbing_section(sid1, cra3, 2, 3)
        route_list = [sec1, sec2, sec3, sec4, sec5, sec6, sec7]

        self.route = Crag(route_list, bot1, top1)
        self.position = self.route.approach_node

        self.is_quitted = False

    def is_won(self) -> bool:
        return self.route.is_summited(self.position)

    def is_lost(self) -> bool:
        return not self.climber.is_alive or ( self.route.is_blind(self.position) and not self.is_won() )

    def quit_game(self) -> None:
        print("You quitted the game.")
        input("Press enter to quit")
        sys.exit()

    def is_finished(self) -> bool:
        return self.is_won() or self.is_lost()
    
    def show_help(self) -> None:
        result = ""
        header = "=== === === === === === HELP for game ERSMS === === === === === ===\n"

        row1 = "You are playing a game about climbing called ERSMS. The game is controlled via terminal.\n"
        row2 = "You can type several commands to progress in the game:\n"
        row3 = " 0, 1, ...   for route options\n"
        row4 = " h           to access help\n"
        row5 = " q           to quit the game\n"
        row6 = " r           to restart the game - NOT IMPLEMENTED YET\n"
        rows = row1 + row2 + row3 + row4 + row5 + row6

        result = header + rows
        print(result)

    def run(self) -> None:
        while True:
            if self.is_finished():
                break
            print("You are in node: ", repr(self.position))
            next_sections = self.route.sections_above(self.position)
            num_next_sec = len(next_sections)

            if not (self.position.protection_possibility == Protection_possibility.NOTHING) and not self.position.protection_used:
                print("Do you wish use a protection?")
                while True:
                    player_input = input("Do you wish use a protection? (y/n)")
                    if player_input == "y":
                        self.route.use_protection(self.position)
                        break
                    elif player_input == "n":
                        break
                    else:
                        print("Invalid input")
                        continue

            print("You can climb:")
            
            for i in range(num_next_sec):
                print(i, next_sections[i])
            
            while True:
                player_input = input("Choose one to climb ")
                if player_input == "h":
                    self.show_help()
                    continue
                if player_input == "q":
                    self.quit_game()
                    break
                
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
            lastNode_prot_used = self.route.nodes_protected[-1]

            if self.climber.attempt_climb(chosen_section):
                self.position = chosen_section.to_node
                self.climber.gain_exp_section(chosen_section)
                chosen_section.change_is_climbed()
            elif lastNode_prot_used == self.position:
                print("You failed to climb a section and now you're back at the begining of the section.")
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
    game = Game()
    game.run()

if __name__ == "__main__":
    main()      