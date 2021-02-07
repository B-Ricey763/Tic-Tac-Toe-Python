from Grid import Grid
from Grid import State

BOARD_SIZE = 3
INPUT_ERR_MSG = "'%s' is not a valid position!"
INPUT_PROMPT_MSG = "Enter a number (1-9) to put an %s or type 'exit' to quit the program. "
EXIT_FLAG = -1

grid = Grid(BOARD_SIZE)
current_mark = State.X

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
    for row in range(grid.size):
        # Initialize our lateral flag
        row_sum = 0
        col_sum = 0

        for col in range(grid.size):
            # Since the enum State has -1 for X and 1 for O, we can add the values
            row_sum += grid.get_value((row, col)).value
            col_sum += grid.get_value((col, row)).value
        if abs(row_sum) == 3 or abs(col_sum) == 3:
            # Someone won the game, the main loop can figure it out
            return True

user_input = get_input(current_mark)

while user_input != EXIT_FLAG:
    coords = (user_input % grid.size, user_input // grid.size)
    grid.set_value(coords, current_mark)

    print(grid)
    current_mark = State.X  if current_mark == State.O else State.O 
    user_input = get_input(current_mark)
        

 