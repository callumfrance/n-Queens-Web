import random
from number_element import NumberElement


class Board:

    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()
        self.queen_list = list()

        for i in range(0, (in_n*in_n)):
            # print(str(i) + " " + str((in_n*in_n)-1))
            self.valid_list.append(NumberElement(i, in_n))

        self._add_next_queen()

    def _add_next_queen(self):
        rand_valid = random.randint(0, len(self.valid_list) - 1)

        removing = self.valid_list[rand_valid]
        self.queen_list.append(removing)
        print(str(removing.row_val) + "\t" + str(removing.col_val))
        print(str(self.queen_list[0].row_val))

        del_row_val = removing.row_val
        del_col_val = removing.col_val
        del_diag11_4_val = removing.diag11_4_val
        del_diag1_8_val = removing.diag1_8_val

        for i in self.valid_list:
            if (i.row_val == del_row_val) or \
                    (i.col_val == del_col_val) or \
                    (i.diag11_4_val == del_diag11_4_val) or \
                    (i.diag11_4_val == del_diag11_4_val):
                self.valid_list.remove(i)

        self._find_next_step()

    def _find_next_step(self):
        if self.queen_counter == self.n:
            self.print_board(True)
        elif not self.valid_list:
            self.print_board(False)
        else:
            self._add_next_queen()

    def print_board(self, full_solution):
        if full_solution:
            print("Full solution found:\n")
        else:
            print("Partial solution found:\n")

        self._print_line_thing()

        for i in range(0, self.n):  # x dimension i.e. rows
            print("|", end=' ')
            for k in range(0, self.n):  # y dimension i.e. columns
                queen_counter = 0
                for queen in self.queen_list:
                    if queen.row_val == i and queen.col_val == k:
                        queen_counter += 1
                if queen_counter == 1:
                    print("Q", end=' ')
                elif queen_counter > 1:
                    print("K", end=' ')  # this should never be reached
                else:
                    print("-", end=' ')
            print("|", end='\n')

        self._print_line_thing()

        print("Number of queens: " + str(len(self.queen_list)))
        for x in range(0, len(self.queen_list)):
            print(str(type(self.queen_list[x].row_val)), end='\t')
            print(str(self.queen_list[x].row_val), end='\t')
            print(str(self.queen_list[x].col_val), end='\n')

        print("Try again? (y/n)")

    def _print_line_thing(self):
        print("+-", end='')
        for i in range(0, self.n):
            print("--", end='')
        print("+", end='\n')
