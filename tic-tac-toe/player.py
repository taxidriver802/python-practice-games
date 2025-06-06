import math, random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    # we want all players to get their next move
    def get_move(self, game):
        pass


class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random square from the available moves
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # check that this is a correct value by
            # trying to cast it to an int, and if its not,
            # then we say its invalid. 
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these two are successful, then this is a valid square
            except ValueError:
                print('Invalid square. Try again.')

        return val

class GeniusPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)               
        
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # random first move
        else:
            # get the square based on the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after that move
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best

        # Ensure the best move is returned
        return best
