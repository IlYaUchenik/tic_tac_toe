import abc  # подключаем библиотеку для работы с абстрактными классами


# класс ячейки
class Cell:
    def __init__(self, value):
        self.value = value

    # проверка на пустоту
    def is_empty(self):
        return self.value == " "

    # очистка
    def clear(self):
        self.value = " "


# класс игрового поля
class Board:
    def __init__(self):
        self.size = 3
        self.cells = []
        self.initialize_board()

    # отображение поля
    def display(self):
        print(self.cells)

    # иницализация поля
    def initialize_board(self):
        self.cells = [
            [Cell(" "), Cell(" "), Cell(" ")][Cell(" "), Cell(" "), Cell(" ")][
                Cell(" "), Cell(" "), Cell(" ")
            ]
        ]

    # сделать ход (задать символ для определенной ячейки)
    def make_move(self, row, col, symbol):
        self.cells[row][col] = symbol

    # проверка на то, что в данную ячейку можно сделать ход
    def is_valid_move(self, row, col):
        if self.cells[row][col] != " ":
            return False
        else:
            return True

    # получить все клетки, в которые можно поставить символ
    def get_available_moves(self):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if available_moves[i][j] == " ":
                    available_moves.append([i, j])
        return available_moves

    # проверка победителя
    def check_winner(self):

        # проверка строк
        for i in range(3):
            if self.cells[i] == [Cell("X"), Cell("X"), Cell("X")] or self.cells[i] == [
                Cell("O"),
                Cell("O"),
                Cell("O"),
            ]:
                return True

        # проверка столбцов
        for i in range(3):
            if (
                self.cells[i][0] == self.cells[i][1]
                and self.cells[i][1] == self.cells[i][2]
            ):
                return True

        # проверка диагоналей
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2]:
            return True
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0]:
            return True

    # проверка на то, что поле полностью заполнено
    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == " ":
                    return False
        return True

    # проверка на то, что игра окончена
    def is_game_over(self):
        if self.check_winner() or self.is_full():
            return True
        else:
            return False

    # создание копии игрового поля (используется для рассчета алгоритма ИИ-шкой)
    def copy(self, name):
        name = self.cells


# абстрактный класс игрока
class Player(abc.ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # абстрактный метод получения текущего хода
    @abc.abstractmethod
    def get_move(self, board):
        pass


# класс человека (нас), наследуемый от класса игрока
class Human(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    # переопределяемый метод получения хода через консоль
    def get_move(self, board):
        row = int(input("Введите строку: "))
        col = int(input("Введите столбец: "))
        if self.is_valid_move(row, col):
            return (row, col)
        else:
            print("Недопустимый ход!")


# класс ИИ, наследуемый от класса игрока
class AIplayer(Player):
    def __init__(self, name, symbol, algorithm):
        super().__init__(name, symbol)
        self.algorithm = algorithm

    # переопределяемый метод для получения хода, который рассчитывается алгоритмом Minimax
    def get_move(self, board):
        # НУЖНО: реализовать метод получения хода исходя из алгоритма Minimax
        pass

    # реализация алгоритма Minimax
    def minimax(self, board, depth, is_maximizing):
        # НУЖНО: реализовать собственно алгоритм Minimax
        pass

    # оценочная функция для алгоритма
    def evaluate_board(board):
        # НУЖНО: реализовать метод для оценки компом следующих ходов
        pass


# класс игры
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.p1 = player1
        self.p2 = player2
        self.current_player = player1
        self.is_game_over = False
        self.winner = None

    # иницализация новой игры с двумя игроками
    def initialize_game(self, player1, player2):
        pass

    # функция переключения текущего игрока
    def switch_player(self):
        if self.current_player == self.p1:
            self.cp = self.p2
        else:
            self.cp = self.p1

    # метод, который запускает игру с ее будущей иницализацией
    def play(self):
        self.p1 = Human("Илюха", "X")
        self.p2 = AIplayer("ИИ", "O")
        self.board.display()
        self.p1.get_move()
        # НУЖНО: добавить получение хода игрока/ИИ,
        # проверять, есть ли еще свободные ячейки в поле
        # если есть, то поставить нужный символ в ячейку,
        # затем сменить текущего игрока
        # иначе - закончить игру
        # ИГРА РЕАЛИЗУЕТСЯ БЕСКОНЕЧНЫМ ЦИКЛОМ ДО ТЕХ ПОР, ПОКА ВСЕ КЛЕТКИ НЕ ЗАНЯТЫ!!!
        # while not is_full(...) or not is_game_over(...):
        #   ...
        #   ...

    def display_result(self):
        print(f"Победитель: {self.winner}")
        pass


# блок объявления игроков (мы, ИИ)
# создание игры
# запуск игры с созданными игроками
# вывод результатов
