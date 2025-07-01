import os

class Game:
    def __init__(self, board=None):
        # Initialize a 3x3 board if not provided
        self.board = board if board else [[' ' for _ in range(3)] for _ in range(3)]

    def save(self, filename="oxogame.dat"):
        """Save the current board to a .dat file as a flat string."""
        with open(filename, 'w') as f:
            flat_board = ''.join(cell for row in self.board for cell in row)
            f.write(flat_board)

    def load(self, filename="oxogame.dat"):
        """Load the board from a .dat file and restore the 3x3 board."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"No saved game found at {filename}")
        with open(filename, 'r') as f:
            flat_board = f.read().strip()
            if len(flat_board) == 9:
                self.board = [list(flat_board[i:i+3]) for i in range(0, 9, 3)]
            else:
                raise ValueError("Invalid game file format.")

    def display(self):
        """Display the current board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, player):
        """Place a player's mark on the board."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def reset(self):
        """Reset the board to the initial empty state."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
