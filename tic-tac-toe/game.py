import time
from player import HumanPlayer, RandomPlayer, GeniusPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep the 3x3 board
        self.current_winner = None # keep track of winner!
    
    def print_board(self):
        for i, row in enumerate([self.board[i*3:(i+1)*3] for i in range(3)]):
            print('| ' + ' | '.join([f"\033[93m{i * 3 + j}\033[0m" if spot == ' ' else spot for j, spot in enumerate(row)]) + ' |')

        
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2  etc (tells us what number corresponds to what box in the board; i.e. 0 is top left, 1 is top middle, etc.)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere... we have to check all possibilities
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [ self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to bottom left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False

    
def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter)! or None for a tie.
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter 
    # iterate while the game still had empty squares
    # (we dont have to worry about winner becasuse we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # function to make a move

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # alternate letters/players after move
            letter = 'O' if letter == 'X' else 'X' 

        #tiny break to smooth out the game
        if print_game:
            time.sleep(0.8)

    if print_game:
            print('It\'s a tie!') 

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    game_reps = 5  # number of games to play in a row

    # 🧠 Player Configuration Guide:
    # - HumanPlayer: you play manually via terminal input
    # - RandomPlayer: basic AI that picks random moves
    # - GeniusPlayer: unbeatable AI using minimax algorithm

    # You can mix and match players:
    # - Play against random AI:        x_player = HumanPlayer('X'), o_player = RandomPlayer('O')
    # - Play against genius AI:        x_player = HumanPlayer('X'), o_player = GeniusPlayer('O')
    # - Watch AI vs. AI (random):      x_player = RandomPlayer('X'), o_player = RandomPlayer('O')
    # - Watch smart AI vs. random AI:  x_player = GeniusPlayer('X'), o_player = RandomPlayer('O')
    # - Watch smart AI vs. smart AI:   x_player = GeniusPlayer('X'), o_player = GeniusPlayer('O')

    # NOTE: X always goes first. Set yourself as x_player if you want to go first.
    x_player = HumanPlayer('X')
    o_player = RandomPlayer('O')

    for _ in range(game_reps):
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=True)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After {game_reps} games we see : X wins: {x_wins}, O wins: {o_wins}, Ties: {ties}')
