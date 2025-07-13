def test_check_winner():
    from game import check_winner
    # Test row win
    board_row = [
        [" X | ", " X | ", " X | "],
        [" | ", " | ", " | "],
        [" | ", " | ", " | "]
    ]
    print("Row win (expect True):", check_winner("X", board_row))

    # Test column win
    board_col = [
        [" O | ", " | ", " | "],
        [" O | ", " | ", " | "],
        [" O | ", " | ", " | "]
    ]
    print("Column win (expect True):", check_winner("O", board_col))

    # Test diagonal win
    board_diag = [
        [" X | ", " | ", " | "],
        [" | ", " X | ", " | "],
        [" | ", " | ", " X | "]
    ]
    print("Diagonal win (expect True):", check_winner("X", board_diag))

    # Test anti-diagonal win
    board_anti_diag = [
        [" | ", " | ", " O | "],
        [" | ", " O | ", " | "],
        [" O | ", " | ", " | "]
    ]
    print("Anti-diagonal win (expect True):", check_winner("O", board_anti_diag))

    # Test no win
    board_no_win = [
        [" X | ", " O | ", " X | "],
        [" O | ", " X | ", " O | "],
        [" O | ", " X | ", " O | "]
    ]
    print("No win (expect False):", check_winner("X", board_no_win))
from game import check_winner
def test_check_winner_row():
    # All cells are 'X', should return True
    board_win = [
        ['X', 'X', 'X'],
        ['X', 'X', 'X'],
        ['X', 'X', 'X']
    ]
    result_win = check_winner('X', board_win)
    print(f"All X board, expect True: {result_win}")

    # One cell is not 'X', should return False
    board_no_win = [
        ['X', 'X', 'O'],
        ['X', 'X', 'X'],
        ['X', 'X', 'X']
    ]
    result_no_win = check_winner('X', board_no_win)
    print(f"One O in board, expect False: {result_no_win}")
import sys
sys.path.append('.')
from game import update_board

def interactive_update_board_test():
    while True:
        try:
            spot = int(input("Enter a spot number (1-9), or 0 to exit: "))
            if spot == 0:
                print("Exiting test.")
                break
            if spot not in range(1, 10):
                print("Please enter a valid spot number between 1 and 9.")
                continue
            row, col = update_board('X', spot, None)
            print(f"Spot {spot} maps to row {row}, column {col}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    #interactive_update_board_test()
    #print("\nTesting check_winner logic:")
    test_check_winner()