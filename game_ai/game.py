import random

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return ' ' not in board

# Function to get the player's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This spot is taken.")
        except (ValueError, IndexError):
            print("Invalid move. Try again.")

# Function for AI's move
def ai_move(board):
    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        
        # AI's turn
        ai_move(board)
        print_board(board)
        if check_win(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
