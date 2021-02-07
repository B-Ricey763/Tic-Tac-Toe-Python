from enum import Enum
from typing import Tuple
from typing import Callable


class State(Enum):
    """Describes the state of any given slot on the grid"""
    EMPTY = 0
    X = -1
    O = 1

class Grid:
    """Wrapper for our Tic Tac Toe Board."""

    def __init__(self, size: int):
        """Creates a new Grid object based on size."""
        self.size = size 
        # Create a 2D array filled with empty state
        self.grid = [[State.EMPTY for x in range(self.size)] for y in range(self.size)]

    def __str__(self):
        grid_str = ""
        # Traverses the grid from left to right, top to bottom
        for row in range(self.size):
            for col in range(self.size):
                # Invert the rows and cols for some reason
                grid_val = self.get_value((col, row))
                state_str = ""
                # Check for the state of each slot
                if grid_val == State.EMPTY:
                    state_str = row * self.size + col + 1
                else:
                    state_str = grid_val.name
                # Generate bars in between the individual marks
                prefix = " | " if 0 < col < self.size else " "
                # Append it onto the string
                grid_str += prefix + str(state_str)
            if row < self.size - 1:
                grid_str += "\n---+---+---\n"
        return grid_str

    def get_value(self, coords: Tuple[int, int]) -> State:
        """Gets the current state of a slot on the grid."""
        return self.grid[coords[1]][coords[0]]

    def set_value(self, coords: Tuple[int, int], val: State) -> None:
        """Sets a slot on the grid to a specific value"""
        self.grid[coords[1]][coords[0]] = val
