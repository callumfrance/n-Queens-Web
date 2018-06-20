class NumberElement:
    """A square inside the board.

    Each square belongs to
        - a column
        - a row
        - each of the two diagonals

    This class was created to remove the simple calculations to determine
    which sets a square belongs to from the board class.
    """

    def __init__(self, in_i, in_n):
        self.row_val = (in_i // in_n) + 1
        self.col_val = (in_i % in_n) + 1
        self.diag11_4_val = in_n - (self.row_val - self.col_val)
        self.diag1_8_val = 2*in_n - (self.row_val + self.col_val) + 1

