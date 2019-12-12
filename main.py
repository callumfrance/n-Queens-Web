import sys
from board import Board
from view import View

"""
python main.py
python main.py cli <n>
python main.py plaintext <n>
python main.py file <n> <filename>
"""

view = ''
a = ''
b = ''
filename = ''


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if (sys.argv[1] == 'cli') 
                or (sys.argv[1] == 'plaintext'
                or (sys.argv[1] == 'file'):
            view = View(sys.argv[1])
    if len(sys.argv) > 2:
        a = int(sys.argv[2])
    if (sys.argv[1] == 'file') and (len(sys.argv) > 3):
            filename = sys.argv[3]
    else:
        print("What 'n' would you like to use?")
        a = int(input("\n> "))

    b = Board(a)
    view.print_board_wrapper(b.full_solution, b.n, b.queen_list)


# TODO add print output to a file with name specified via the cli
