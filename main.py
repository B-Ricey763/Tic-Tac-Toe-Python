from Grid import Grid
from Grid import State

BOARD_SIZE = 3
INPUT_ERR_MSG = "'%s' is not a valid position!"
INPUT_PROMPT_MSG = "Enter a number (1-9) to put an %s or type 'exit' to quit the program. "
EXIT_FLAG = -1
MAX_TURNS = 9

def get_input(mark: State) -> int:    
    """Gets raw input from cmd."""
    user_input = input(INPUT_PROMPT_MSG % mark.name).strip() # Remove extra spaces

    if user_input != "exit":
        try: 
            int_input = int(user_input) - 1
            # Make sure input is in valid range (if, not error raises into our except block)
            assert 0 <= int_input <= 8
            return int_input
        except:
            # Tell them invalid input and do some recursion
            print(INPUT_ERR_MSG % user_input)
            return get_input(mark)
    return EXIT_FLAG # Notify the loop  to stop


def detect_win(grid: Grid) -> bool:
    diag_sum = 0
    anti_diag_sum = 0

    # Iterate through entire board
    for row in range(grid.size):
        # Initialize our lateral flag
        row_sum = 0
        col_sum = 0

        for col in range(grid.size):
            # Since the enum State has -1 for X and 1 for O, we can add the values
            row_sum += grid.get_value((row, col)).value
            col_sum += grid.get_value((col, row)).value

            if row == col:
                diag_sum += grid.get_value((row, col)).value
            if row + col == 2:
                anti_diag_sum += grid.get_value((row, col)).value

        if grid.size in (abs(row_sum), abs(col_sum), abs(diag_sum), abs(anti_diag_sum)):
            # Someone won the game, the main loop can figure it out
            return True
    return False

replay_input = "y"

while replay_input == "y":

    grid = Grid(BOARD_SIZE)
    current_mark = State.X
    win = False
    user_input = 0 # default to start while loop
    turn_count = 0

    while not win and turn_count < MAX_TURNS:
        # Toggle state of the mark
        current_mark = State.X  if current_mark == State.O else State.O 
        # User Interfacing
        print(grid)
        user_input = get_input(current_mark)
        if user_input == EXIT_FLAG:
            break
        # Applying changes to our grid
        coords = (user_input % grid.size, user_input // grid.size)
        grid.set_value(coords, current_mark)
        win = detect_win(grid)
        turn_count += 1

    if user_input == EXIT_FLAG:
        break
    
    print(grid)
    if win:
        print(current_mark.name + " won the game!")
    else:
        print("It was a draw!")
    replay_input = input("Would you like to play again? (y/n)").strip()
        

 