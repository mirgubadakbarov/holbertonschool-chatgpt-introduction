def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-------")

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        col_values = [board[row][col] for row in range(len(board))]
        if col_values.count(col_values[0]) == len(col_values) and col_values[0] != " ":
            return col_values[0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    # Check if the board is full and there is no winner
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
