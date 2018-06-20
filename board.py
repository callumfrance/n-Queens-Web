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
    """

    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()
        self.queen_list = list()

        for i in range(in_n*in_n):
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

        for i in range(len(self.valid_list)-1, -1, -1):
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
            self.print_board(True)
        elif not self.valid_list:
            self.print_board(False)
        else:
            self._add_next_queen()

    def print_board(self, full_solution):
        """Formats the board for printing.

        Parameters
        ----------
            full_solution : boolean
                A flag that determines what kind of solve has been achieved.
        """
        if full_solution:
            print("Full solution found:\n")
        else:
            print("Partial solution found:\n")

        self._print_line_thing()

        for i in range(self.n):  # x dimension i.e. rows
            print("|", end=' ')
            for k in range(self.n):  # y dimension i.e. columns
                queen_counter = 0
                for queen in self.queen_list:
                    if queen.row_val == i + 1 and queen.col_val == k + 1:
                        queen_counter += 1
                if queen_counter == 1:
                    print("Q", end=' ')
                elif queen_counter > 1:
                    print("K", end=' ')  # this should never be reached
                else:
                    print("-", end=' ')
            print("|", end='\n')

        self._print_line_thing()

        print("\nn: " + str(self.n))
        print("Number of queens: " + str(len(self.queen_list)))
        print("\nTry again? (y/n)")

    def _print_line_thing(self):
        """Small thingy to format the edges of the board.
        """
        print("+-", end='')
        for i in range(0, self.n):
            print("--", end='')
        print("+", end='\n')
