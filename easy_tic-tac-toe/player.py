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
               
        
   