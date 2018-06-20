class NumberElement:

    def __init__(self, in_i, in_n):
        self.row_val = ((in_i - 1) // in_n) + 1
        self.col_val = ((in_i - 1) % in_n) + 1
        self.diag11_4_val = in_n - (self.row_val - self.col_val)
        self.diag1_8_val = 2*in_n - (self.row_val + self.col_val) + 1


"""
11-4

(3,3) = 5 = 5 - (3-3)
(1,4) = 2 = 5 - (4-1)

(3,1) = 7 = 5 - (1-3)


1-8

(4,3) = 4 = 2*5 - (4+3) + 1

(2,5) = 4 = 2*5 - (2+5) + 1

(5,5) = 1 = 2*5 - (5+5) + 1

"""
