import random
from number_element import NumberElement


class Board:

    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()
        self.queen_list = list()

        for i in range(in_n*in_n):
            self.valid_list.append(NumberElement(i, in_n))
            # print("[" + str(self.valid_list[i].col_val) + ", " + str(self.valid_list[i].row_val), end='; ')
            # print(str(self.valid_list[i].diag11_4_val) + ", " + str(self.valid_list[i].diag1_8_val), end=']\n')

        self._add_next_queen()

    def _add_next_queen(self):
        rand_valid = random.randint(0, len(self.valid_list) - 1)

        removing = self.valid_list[rand_valid]
        self.queen_list.append(removing)
        print("queened: " + str(removing.col_val) + ", " + str(removing.row_val), end=' ')
        print("; " + str(removing.diag11_4_val) + ", " + str(removing.diag1_8_val), end='\n')

        print("Current queen list: ")
        for i in range(len(self.queen_list)):
            print("\t[" + str(self.queen_list[i].col_val) + ", " + \
                    str(self.queen_list[i].row_val) + "]")

        del_row_val = removing.row_val
        del_col_val = removing.col_val
        del_diag11_4_val = removing.diag11_4_val
        del_diag1_8_val = removing.diag1_8_val

        print("Removed: ", end='\n')
        for i in self.valid_list:
            print("[" + str(i.col_val) + ", " + str(i.row_val), end='; ')
            print(str(i.diag11_4_val) + ", " + str(i.diag1_8_val) + "]", end=' ')
            if (i.row_val == del_row_val) or \
                    (i.col_val == del_col_val) or \
                    (i.diag11_4_val == del_diag11_4_val) or \
                    (i.diag11_4_val == del_diag11_4_val):
                self.valid_list.remove(i)
                print("\tremoved")
            else:
                print("\tstays")
        print("\n")

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

        print("Number of queens: " + str(len(self.queen_list)))
        for x in range(0, len(self.queen_list)):
            print(str(type(self.queen_list[x].row_val)), end='\t')
            print(str(self.queen_list[x].col_val), end='\t')
            print(str(self.queen_list[x].row_val), end='\n')

        print("Try again? (y/n)")

    def _print_line_thing(self):
        print("+-", end='')
        for i in range(0, self.n):
            print("--", end='')
        print("+", end='\n')
