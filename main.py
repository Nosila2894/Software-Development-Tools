from engine import Engine
from states import *
from data import DataManager


def main():
    data = DataManager("data")

    game = Engine(data=data)

    game.register_state("TITLE_SCREEN", TitleScreen)
    game.register_state("OPTIONS", Options)
    game.register_state("CHARACTER_CREATION", CharacterCreation)

    game.set_start_state("TITLE_SCREEN")

    game.run()

if __name__ == "__main__":
    main()

    input("\nPress ENTER to close the Game Window...")