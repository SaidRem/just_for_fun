# Tic Tac Toe game.
# Rules are simple: two person marks 9 cells in their turn.
# The winner is the one with a match in a row or diagonally.

def get_blank_board():
    """Create a new, blank tic tac toe board."""
    board = {}   # Let's represent the board as a dictionary.
    for space in range(1, 10):
        board[space] = ' '  # All spaces start as blank.
    return board


def get_board_string(board):
    """Return a text-representation of the board."""
    return '''
              {}|{}|{}  1 2 3
              -+-+-
              {}|{}|{}  4 5 6
              -+-+-
              {}|{}|{}  7 8 9'''.format(board[1], board[2], board[3],
                                        board[4], board[5], board[6],
                                        board[7], board[8], board[9])


def is_valid_space(board, space):
    """Returns True if the space on the board is a valid space number
       and the space is blank."""
    return space in range(1, 10) and board[space] == ' '


def is_winner(board, player):
    """Return True if player is a winner on this board."""
    return ((board[1] == board[2] == board[3] == player) or
            (board[4] == board[5] == board[6] == player) or
            (board[7] == board[8] == board[9] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[3] == board[6] == board[9] == player) or
            (board[3] == board[5] == board[7] == player) or
            (board[1] == board[5] == board[9] == player)
            )


def is_board_full(board):
    """Return True if every space on the board has been taken."""
    for space in range(1, 10):
        if board[space] == ' ':
            return False  # If a single space is blank, return False.
    return True  # No spaces are blank, so return True.


def update_board(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


def main():
    """Runs the game."""
    game_board = get_blank_board()  # Create a board dictionary.
    current_player, next_player = "X", "O"    # "X" - first player, "O" - second player. 
    # Create loop that asks players until they enter a number.
    while True:    
        print(get_board_string(game_board))
        move = None
        while not is_valid_space(game_board, move):
            print(f'What is {current_player} move? (1-9)')
            move = int(input())
        update_board(game_board, move, current_player)
        if is_winner(game_board, current_player):    # Checks for victory.
            print(get_board_string(game_board))
            print(current_player + ' has won the game!')
            break
        elif is_board_full(game_board):     # Checks for a tie.
            print(get_board_string(game_board))
            print('The game is a tie!')
            break
        current_player, next_player = next_player, current_player    # Swaps turns of the players.
    print('THE END')


if __name__ == '__main__':
    main()
