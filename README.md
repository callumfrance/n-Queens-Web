nQueens
-------

This program randomly places queens on a chess board so that no queen will
be able to capture another queen.
The number of Queens for a 'full solve' is equal to the dimensions of the
board - i.e. an 8x8 board has a full solve of 8 queens.
This program places Queens randomly, so using numbers bigger than 5 will
almost certainly only give a partial solve.


Also note that nQueens is impossible for `n = 3` or `n = 4` (which you can
see by running the program).


1. Create Board using 'n'
	- create n^2 elements
		- each element is placed in a grid formation on the board
		- each element is set to hasQueen = False
	- create a queen counter = 0
	- create a 'valid' set of the n^2 elements
		- initially, this holds every single element

2. Assign a random valid element to have a queen
	- decrease queen counter
	ROW
		- remove every element on the same row from the valid set
	COLUMN
		- remove every element on the same column from the valid set
	DIAG11_4
		- remove every element on the same diagonal from the valid set
	DIAG1_8
		- remove every element on the same diagonal from the valid set

3. Find next step
	- if queen counter has reached n, exit and print final board
	- if every element is invalid, exit and print the partial solution
	- if there are still some valid elements, repeat step 2
