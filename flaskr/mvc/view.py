# Set of possible display types
display_types = ('cli', 'plaintext', 'file', 'html')


class View:
    """How the program is displayed to the user.

    The program can be displayed via the command line interface, using `print`.

    It could also be displayed other ways
    """
    def __init__(self, in_disp_type="cli", output_file_name=None):
        if in_disp_type in display_types:
            self.disp_type = in_disp_type
        else:
            self.disp_type = display_types[0]
        if output_file_name:
            self.output_file_name = output_file_name

    def print_board_html(self, full_solution, n, queen_list):
        """Returns a string view of the n-Queens board.
        """
        print_board_val = ''
        if full_solution:
            print_board_val += "Full solution found:<br><br>"
        else:
            print_board_val += "Partial solution found:<br><br>"

        print_board_val += self._print_line_thing_html(n)

        for i in range(n):  # x dimension i.e. rows
            print_board_val += '<span class="board edge vertical">|</span> '
            for k in range(n):  # y dimension i.e. columns
                queen_counter = 0
                for queen in queen_list:
                    if queen.row_val == i + 1 and queen.col_val == k + 1:
                        queen_counter += 1
                if queen_counter == 1:
                    print_board_val += '<span class="board queen">Q</span> '
                elif queen_counter > 1:  # this should never be reached
                    print_board_val += '<span class="board king">K</span> '
                else:
                    print_board_val += '<span class="board blank">-</span> '
            print_board_val += '<span class="board edge vertical">|</span><br>'

        print_board_val += self._print_line_thing_html(n)

        return print_board_val

    def print_board_plaintext(self, full_solution, n, queen_list):
        """Returns a string view of the n-Queens board.
        """
        print_board_val = ''
        if full_solution:
            print_board_val += "Full solution found:\n\n"
        else:
            print_board_val += "Partial solution found:\n\n"

        print_board_val += self._print_line_thing_plaintext(n)

        for i in range(n):  # x dimension i.e. rows
            print_board_val += "| "
            for k in range(n):  # y dimension i.e. columns
                queen_counter = 0
                for queen in queen_list:
                    if queen.row_val == i + 1 and queen.col_val == k + 1:
                        queen_counter += 1
                if queen_counter == 1:
                    print_board_val += "Q "
                elif queen_counter > 1:
                    print_board_val += "K "  # this should never be reached
                else:
                    print_board_val += "- "
            print_board_val += "|\n"

        print_board_val += self._print_line_thing_plaintext(n)

        return print_board_val

    def print_board_wrapper(self, full_solution, n, queen_list):
        """Directs to the correct printing type as specified by self.disp_type.
        """
        print_val = self.print_board_plaintext(full_solution, n, queen_list)
        if self.disp_type == 'cli':
            print(print_val)
        elif self.disp_type == 'plaintext':
            pass
        elif self.disp_type == 'file':
            with open(self.output_file_name, "a") as f:
                f.write(print_val)
        elif self.disp_type == 'html':
            print_val = self.print_board_html(full_solution, n, queen_list)
        return print_val

    def _print_line_thing_html(self, n):
        """Small thingy to format the edges of the board.
        
        Formatted in HTML using span tags and the following classes:
            {board, corner, edge, horizontal}
        """
        line_val = ''
        line_val += '<span class="board corner">+</span>'
        line_val += '<span class="board edge horizontal>-</span>'
        for i in range(0, 4*n):
            line_val += '<span class="board edge horizontal>-</span>'
        line_val += '<span class="board corner">+</span><br>'

        return line_val

    def _print_line_thing_plaintext(self, n):
        """Small thingy to format the edges of the board.
        """
        line_val = ''
        line_val += '+-'
        for i in range(0, n):
            line_val += '--'
        line_val += '+\n'

        return line_val
