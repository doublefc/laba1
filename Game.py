class Game:

    def __init__(self,  available_games, n_trials=3, n_rounds=3):
        self.n_rounds = n_rounds
        self.available_games = available_games
        self.n_trials = n_trials

    def __base_io(self):
        print('Привет! Добро пожаловать в Brain Games!')

        self.name = input('Как тебя зовут?')
        self.game_str = input(
        f'В какую игру из списка: \n {" ".join(list(self.available_games.keys()))}'+\
            ' \n ты хочешь поиграть?')\
                .lower()
        if self.game_str.isnumeric():
            self.game_str = list(self.available_games.keys())[int(self.game_str)-1]

    def launch(self, new_user=True):
        if new_user:
            self.__base_io()

        for _ in range(self.n_rounds):
            question, right_answer = self.available_games[self.game_str]()
            for _ in range(self.n_trials):
                user_answer_float = float(input(question + '\n Твой ответ:'))
                if user_answer_float == right_answer:
                    print('Молодец, верно')
                    break
                else:
                    print('Попытайся еще')
            else:
                print(f'Кол-во попыток кончилось, правильный ответ был {right_answer}')











