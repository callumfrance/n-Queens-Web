import sys
from .board import Board
from .view import View
"""
Examples of ways to execute the program:
    python main.py
    python main.py cli <n>
    python main.py plaintext <n>
    python main.py file <n> <filename>

Systems arguments:
    sys.arg[1] : view type {'cli', 'plaintext', 'file'}
    sys.arg[2] : size of n
    sys.arg[3] : filename (only used and required for view type 'file')

This is the main file of the program, it also acts as the controller.
"""

n_size = 0
b = ''
filename = ''

def determine_view(view_string, filename=None):
    if (view_string == 'cli') \
            or (view_string == 'plaintext'):
        view = View(view_string)

    elif (view_string == 'file'):
        if (filename):
            view = View(view_string, filename)
        else:  # Default the filename as 'output.txt'
            view = View(view_string, "output.txt")

    else:  # Default the view to be using the command line interface
        view = View('cli')
    
    return view


def run_n_queens(view_string, n_size, filename=None):
    view = determine_view(view_string, filename)
    b = Board(n_size)
    board_view_str = view.print_board_wrapper(b.full_solution, b.n, b.queen_list)

    return board_view_str


if __name__ == "__main__":
    if len(sys.argv) > 2:
        n_size = int(sys.argv[2])
    else:
        print("What 'n' would you like to use?")
        n_size = int(input("\n> "))

    if len(sys.argv) > 3:
        run_n_queens(sys.argv[1], n_size, sys.argv[3])
    elif len(sys.argv) > 1:
        run_n_queens(sys.argv[1], n_size)
    else:
        run_n_queens('cli', n_size)


