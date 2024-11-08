
from games import nok, geom_progression
from Game import Game

def main():
    available_games = {'Геометрическая прогрессия': geom_progression.geom_progression, 'Наименьшее общее кратное': nok.nok}

    game = Game(available_games)
    for i in range(len(available_games)):
        game.launch()

if __name__ == "__main__":
    main()