"Build a text-based version of the Tic Tac Toe game."
#solution
# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there is a win or a draw
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    if [player, player, player] in win_conditions:
        return True
    return False

# Function to check for a draw
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        move = input("Enter your move (row and column: 1 1): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        row, col = int(move[0]) - 1, int(move[1]) - 1

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Place the player's move on the board
        board[row][col] = current_player

        # Check if the player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if it's a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
