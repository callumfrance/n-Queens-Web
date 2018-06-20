import random
from number_element import NumberElement


class Board:

    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()
        self.queen_list = list()

        for i in range(0, n*n-1):
            self.valid_list[i] = NumberElement(i, n)

        self._add_next_queen()

    def _add_next_queen(self):
        rand_valid = randint(0, len(self.valid_list))

        removing = self.valid_list[rand_valid]
        self.queen_list.append(removing)

        del_row_val = removing.row_val
        del_col_val = removing.col_val
        del_diag11_4_val = removing.diag11_4_val
        del_diag1_8_val = removing.diag1_8_val

        for i in self.valid_list:
            if (i.row_val = del_row_val) or \
                    (i.col_val = del_col_val) or \
                    (i.diag11_4_val = del_diag11_4_val) or \
                    (i.diag11_4_val = del_diag11_4_val):
                self.valid_list.remove(i)

        self.find_next_step()

    def _find_next_step(self):
        if self.queen_counter = n:
            self.print_board(True)
        elif not self.valid_list:
            self.print_board(False)
        else:
            self.add_next_queen()

    def print_board(self, full_solution):
        if full_solution:
            print("Full solution found:\n")
        else:
            print("Partial solution found:\n")

        self._print_line_thing()

        for i in range(0, n):  # x dimension i.e. rows
            print("|", end=' ')
            for k in range(0, n):  # y dimension i.e. columns
                for queen in self.queen_list:
                    if queen.row_val == i and queen.col_val == k:
                        print("Q", end=' ')
                    else:
                        print("-", end=' ')
            print("|", end='\n')

        self._print_line_thing()

        print("Try again? (y/n)")

    def _print_line_thing(self):
        print("+-", end='')
        for i in range(0, n):
            print("--", end='')
        print("+", end='\n')
