import tkinter as tk
import random

class BinaryBoardGameGUI:
    def __init__(self, root, size=5):
        self.size = size
        self.root = root
        self.root.title("Binary Board Game")

        # Generate initial board and target board
        self.board = self.generate_board()
        self.target = self.generate_board()

        # Create the GUI grid
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_board()

        self.current_board_label = tk.Label(self.root, text="Current Board:")
        self.current_board_label.grid(row=self.size, column=0, columnspan=self.size, pady=10)

        self.target_board_label = tk.Label(self.root, text="Target Board:")
        self.target_board_label.grid(row=self.size + 1, column=0, columnspan=self.size, pady=10)

        self.win_label = tk.Label(self.root, text="")
        self.win_label.grid(row=self.size + 2, column=0, columnspan=self.size)

        # Display initial boards
        self.display_target_board()
        self.display_current_board()

    def generate_board(self):
        """Generate a random 0-1 board."""
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def create_board(self):
        """Create the board in the GUI with buttons."""
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.root, text=str(self.board[i][j]), width=5, height=2,
                                   command=lambda i=i, j=j: self.flip_square(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def flip_square(self, i, j):
        """Flip the square at (i, j) and update the board."""
        self.board[i][j] = 1 - self.board[i][j]
        self.update_button(i, j)
        self.display_current_board()

        if self.is_game_over():
            self.display_win_message()

    def update_button(self, i, j):
        """Update the button text after flipping."""
        self.buttons[i][j].config(text=str(self.board[i][j]))

    def display_current_board(self):
        """Display the current board state."""
        self.current_board_label.config(text="Current Board:" + "\n" + self.board_to_string(self.board))

    def display_target_board(self):
        """Display the target board state."""
        self.target_board_label.config(text="Target Board:" + "\n" + self.board_to_string(self.target))

    def board_to_string(self, board):
        """Convert a board to a string format for display."""
        return "\n".join([' '.join(map(str, row)) for row in board])

    def is_game_over(self):
        """Check if the current board matches the target."""
        return self.board == self.target

    def display_win_message(self):
        """Display a win message when the game is over."""
        self.win_label.config(text="Congratulations! You won the game!")

# Set up the Tkinter window
root = tk.Tk()

# Create the game instance with a 5x5 board
game = BinaryBoardGameGUI(root, size=5)

# Start the Tkinter main loop
root.mainloop()
