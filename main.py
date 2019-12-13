import sys
from board import Board
from view import View
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

view = ''
a = ''
b = ''
filename = ''

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if (sys.argv[1] == 'cli') \
                or (sys.argv[1] == 'plaintext'):
            view = View(sys.argv[1])

        elif (sys.argv[1] == 'file'):
            filename = sys.argv[3]
            if (len(sys.argv) > 3):
                view = View(sys.argv[1], sys.argv[3])
            else:  # Default the filename as 'output.txt'
                view = View(sys.argv[1], "output.txt")
    else:  # Default the view to be using the command line interface
        view = View('cli')

    if len(sys.argv) > 2:
        a = int(sys.argv[2])

    else:
        print("What 'n' would you like to use?")
        a = int(input("\n> "))

    b = Board(a)
    view.print_board_wrapper(b.full_solution, b.n, b.queen_list)
