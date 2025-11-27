#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_input(player, axis):
    while True:
        try:
            value = int(input(f"Enter {axis} (0, 1, or 2) for player {player}: "))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid number! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # SAFE input for row & column
        row = get_input(player, "row")
        col = get_input(player, "column")

        # Ensure the spot is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check win
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
