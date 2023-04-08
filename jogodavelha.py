class CreateGame:

    def save_play(self, matrix: list[list[any]], 
        player: str, line: int, column: int) -> list[int]:
        if matrix[line][column] == 0:
            matrix[line][column] = player
            return matrix
        else: 
            print("Esse quadrado já foi marcado!")
            return player

    def create_matrix(self) -> list[list[int]]:
        matrix = [[0, 0, 0] for j in range(3)]
        return matrix

    def play(self) -> dict:
        played = {}
        played["line"] = int(input('Em qual linha você quer jogar? (0/1/2)'))
        played["column"] = int(input('Em qual coluna você quer jogar? (0/1/2)'))
        return played

    def define_player(self, num_play: int) -> str:
        if num_play % 2 == 0:
            return -1
        else:
            return 1

    def winner(self, matrix: list[list[any]]) -> str:
        for idx in range(3):

            if (matrix[idx][0] + matrix[idx][1] + matrix[idx][2] == 3 
                or matrix[0][idx] + matrix[1][idx] + matrix[2][idx] == 3):
                return "X"

            elif (matrix[idx][0] + matrix[idx][1] + matrix[idx][2] == -3
                or matrix[0][idx] + matrix[1][idx] + matrix[2][idx] == -3):
                return "O"

        if (matrix[0][0] + matrix[1][1] + matrix[2][2] == 3 
            or matrix[2][0] + matrix[1][1] + matrix[0][2] == 3):
            return "X"

        elif (matrix[0][0] + matrix[1][1] + matrix[2][2] == -3
            or matrix[2][0] + matrix[1][1] + matrix[0][2] == -3):
            return "O"

        else:
            return None

    def show_matrix(self, matrix: list[list[int]]) -> None:
        for line in range(3):
            for column in range(3):
                if matrix[line][column] == 1:
                    print(" X ", end="")
                elif matrix[line][column] == -1:
                    print(" O ", end="")
                else:
                    print(" _ ", end="")
            print("\n")

    def the_winner(self, winner):
        if winner == "X":
            return "O vencedor é o jogador X!"
        elif winner == "O":
            return "O vencedor é o jogador X!"
        else:
            return "Deu velha! :("

    
class Play(CreateGame):
    def __init__(self):
        self.initial_matrix = self.create_matrix()
        self.show_matrix(self.initial_matrix)
        self.is_playing()

    def is_playing(self):
        play = 1
        winner = None
        while play <= 10 and not winner:

            print("="*10)
            print(f"Jogada {play}")
            print("="*10)

            player = self.define_player(play)
            played = self.play()
            
            saved_play = self.save_play(self.initial_matrix, player, 
                played['line'], played['column'])

            if saved_play == player:
                continue
            
            self.initial_matrix = saved_play

            self.show_matrix(self.initial_matrix)

            winner = self.winner(self.initial_matrix)
            play += 1

        print(self.the_winner(winner))

Play()