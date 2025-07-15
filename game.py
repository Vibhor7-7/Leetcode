### Tic Tac Toe Game 
import sys
import random 

def main():

    #Default Values 
    board = create_board()
    curr_player = "X"
    mode = game_mode()

    #Game Loop
    while mode == "1v1":
        game_state(board)

        spot = get_move(curr_player)
        board = update_board(curr_player, spot, board)

        winner = check_winner(curr_player, board)
        if winner:
            game_state(board)
            print(f'{curr_player} has won the game')
            break

        tie = check_tie(board)
        if tie:
            game_state(board)
            print(f'The game has ended in a tie')
            break
        # Switch player
        curr_player = 'O' if curr_player == 'X' else 'X'
    
    while mode =="Against AI":
        game_state(board)

        if curr_player == "X":
            spot = get_move(curr_player)
            board = update_board(curr_player, spot, board)
        else:
            print("AI is thinking...")
            board = smart_ai(board, curr_player)
            game_state(board)
            print('AI has made its move')
    

        winner = check_winner(curr_player, board)
        if winner:
            game_state(board)
            print(f'{curr_player} has won the game')
            break

        tie = check_tie(board)
        if tie:
            game_state(board)
            print(f'The game has ended in a tie')
            break
        # Switch player
        curr_player = 'O' if curr_player == 'X' else 'X'


def create_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def game_state(board):
   for i,row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--" * 5)

def get_move(curr_player):
    print(f'{curr_player} Where do you want to move: 1-9' )
    while True:
        try:
            spot = int(input())
            if spot in range(1, 10):
                return spot
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def update_board(curr_player, spot, board):
    # Convert the spot to row and column indices
    
        if spot == 1:
            row, col = 0,0 
        remainder = spot % 3
        if remainder == 0:
            col = 2
            row = spot //3 - 1 
        else:
            col = remainder - 1
            row = spot // 3
        if board[row][col] == " ":
            board[row][col] = f"{curr_player}"
        else:
            print("That spot is already taken. Please choose another spot.")
            return update_board(curr_player, get_move(curr_player), board)
        return board
        

def check_winner(curr_player, board):
    # Check if someone got 3 in a row
        for row in board:
           if row[0] == row[1] == row[2] != " ":
                  return True    
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True 
        else: 
            return False 

def check_tie(board):
    #check if the board is full 
    for row in board:
        for col in row: 
            if col == " ":
                return False 
    return True 


def game_mode():
    mode = input("What would you like to play: 1v1 or Against AI\n")
    if mode == '1v1':
        return mode 
    elif mode == 'Against AI':
        return mode 
    else: 
        print("Invaild Input, please indicate 1v1 or Against AI")
        return game_mode()


def random_ai(board, curr_player):
    rand_spot = random.randint(1,9)
    if rand_spot == 1:
        row, col = 0,0 

    remainder = rand_spot % 3

    if remainder == 0:
        col = 2
        row = rand_spot //3 - 1 
    else:
        col = remainder - 1
        row = rand_spot // 3
    if board[row][col] == " ":
        board[row][col] = f"{curr_player}"
    else :
        print("AI picked a spot that was already taken. Choosing another spot.")
        return random_ai(board, curr_player)
    return board


def smart_ai(board, curr_player):
    # First check if AI can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # Try the move
                board[i][j] = curr_player
                if check_winner(curr_player, board):
                    return board
                # Undo the move
                board[i][j] = " "
    # Then check if AI needs to block opponent's winning move
    opponent = "O" if curr_player == "X" else "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # Try the move
                board[i][j] = opponent
                if check_winner(opponent, board):
                    board[i][j] = curr_player
                    return board
                # Undo the move
                board[i][j] = " "       

    
    # If no winning move or blocking move, play randomly
    return random_ai(board, curr_player)


def minmax_ai(board, curr_player):
    ... # Implement Minimax algorithm for AI
if __name__ == "__main__":
    main()