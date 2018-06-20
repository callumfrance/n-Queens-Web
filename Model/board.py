import random
from number_element import NumberElement

class Board:

    def __init__(self, in_n):
        self.n = in_n
        self.queen_counter = 0
        self.valid_list = list()

        for i in range(0, n*n-1):
            self.valid_list[i] = NumberElement(i, n)

    def add_next_queen(self):
        rand_valid = randint(0, len(self.valid_list))

        removing = self.valid_list[rand_valid]

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

    def find_next_step(self):
        if self.queen_counter = n:
            # Successfully finished program
            pass
        elif not self.valid_list:
            # Partial solution found
            pass
        else:
            self.add_next_queen()
