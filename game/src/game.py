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

        self.route = Crag(route_list, bot1, top1)
        self.position = self.route.approach_node

        self.is_quitted = False

    def is_won(self) -> bool:
        return self.route.is_summited(self.position)

    def is_lost(self) -> bool:
        return not self.climber.is_alive or ( self.route.is_blind(self.position) and not self.is_won() )

    def is_quitted(self) -> bool:
        return self.is_quitted
    
    def quit_game(self) -> None:
        self.is_quitted = True

    def is_finished(self) -> bool:
        return self.is_won() or self.is_lost() or self.is_quitted
    
    def show_help(self) -> None:
        print("=== === === === === === HELP for game ERSMS === === === === === ===")
        print("You are playing a game about climbing called ERSMS. The game is controlled via terminal.")
        print("You can type several commands to progress in the game:")
        print(" 0, 1, ...   for route options")
        print(" h           to acces help")
        print(" q           to quit the game")
        print(" r           to restart the game - NOT IMPLEMENTED YET")
        

    def run(self) -> None:
        while True:
            if self.is_finished():
                break
            print("You are in node: ", self.position)
            next_sections = self.route.sections_above(self.position)
            num_next_sec = len(next_sections)
            print("You can climb:")
            
            for i in range(num_next_sec):
                print(i, next_sections[i])
            
            while True:
                player_input = input("Choose one to climb ")
                if player_input == "h":
                    self.show_help()
                    break
                if player_input == "q":
                    self.quit_game
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
            

            next_section = next_sections[choice]

            if self.climber.can_climb(next_section):
                self.position = next_section.to_node
            else:
                self.climber.die()
            # TODO: spadl a umrel > konec hry

        if self.is_won():
            print("VICTORY!")
        elif self.is_lost():
            print("Try again")
        else:
            print("You quitted the game.")
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()      