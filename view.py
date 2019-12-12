class View:
	"""How the program is displayed to the user.

	The program can be displayed via the command line interface, using `print`.

	It could also be displayed other ways
	"""

	display_types = ('cli', 'plaintext')

	def __init__(self, in_disp_type="cli"):
		if in_disp_type in display_types:
			self.disp_type = in_disp_type
		else:
			self.disp_type = display_types[0]


#	def print_menu_wrapper(self):
#		print_val = "What 'n' would you like to use?"
#		if self.disp_type = 'cli':
#			print(print_val)
#		else if self.disp_type 'plaintext':
#			return print_val

	
	def print_board_wrapper(self):
		print_val = ''
		if self.disp_type = 'cli':
			print(print_board_plaintext())
		else if self.disp_type = 'plaintext':
			print_val = print_board_plaintext()
		return print_val

	
    def print_board_plaintext(self, full_solution, n, queen_list):
		print_board_val = ''
        if full_solution:
			print_board_val += "Full solution found:\n\n"
        else:
			print_board_val += "Partial solution found:\n\n"

        print_board_val += self._print_line_thing_plaintext()

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
					print_board_val += "K " # this should never be reached
                else:
					print_board_val += "- "
			print_board_val += "|\n"

        print_board_val += self._print_line_thing_plaintext()

		return print_board_val


    def _print_line_thing_plaintext(self, n):
        """Small thingy to format the edges of the board.
        """
		line_val = ''
		line_val += '+-'
        for i in range(0, n):
			line_val += '--'
        print("+", end='\n')
		line_val += '+'

		return line_val
