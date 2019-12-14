import random
from number_element import NumberElement


class Board:
    """
    Attributes
    ----------
        n : int
            The dimensions of the board and the number of queens for full solve

        queen_counter : int
            The number of queens currently on the board.

        valid_list : list<NumberElement>
            The number of valid remaining spaces.

        queen_list : list<NumberElement>
            The squares that contain queens so far.

        full_solution: Boolean
            Identifies if this board contains a full 'n' solution.
    """
    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()
        self.queen_list = list()
        self.full_solution = False

        for i in range(in_n * in_n):
            self.valid_list.append(NumberElement(i, in_n))

        self._add_next_queen()

    def _add_next_queen(self):
        """Randomly adds a queen to any valid square

        Adds the chosen queen to the queen list and to the queen counter.
        Retrieves all values that would create a conflict set from the square
        Then removes any conflicting squares from the valid_list.
        This ensures that no conflicting square is randomly selected later.
        """
        rand_valid = random.randint(0, len(self.valid_list) - 1)

        removing = self.valid_list[rand_valid]
        self.queen_list.append(removing)
        self.queen_counter += 1

        del_row_val = removing.row_val
        del_col_val = removing.col_val
        del_diag11_4_val = removing.diag11_4_val
        del_diag1_8_val = removing.diag1_8_val

        for i in range(len(self.valid_list) - 1, -1, -1):
            if (self.valid_list[i].row_val == del_row_val) or \
                    (self.valid_list[i].col_val == del_col_val) or \
                    (self.valid_list[i].diag11_4_val == del_diag11_4_val) or \
                    (self.valid_list[i].diag1_8_val == del_diag1_8_val):
                del self.valid_list[i]

        self._find_next_step()

    def _find_next_step(self):
        """Will determine if the exit condition has been reached or not.
        """
        if self.queen_counter == self.n:
            self.full_solution = True
            return (self)
        elif not self.valid_list:
            self.full_solution = False
            return (self)
        else:
            self._add_next_queen()
