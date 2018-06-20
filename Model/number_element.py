class NumberElement:

    def __init__(self, in_i, in_n):
        self.has_queen = False
        self.row_val = ((in_i - 1) // in_n) + 1
        self.col_val = ((in_i - 1) % in_n) + 1
        self.diag11_4_val
        self.diag1_8_val
