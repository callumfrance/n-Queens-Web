from board import Board


if __name__ == "__main__":
    to_exit = False

    while not to_exit:
        b = Board()

        c = input("\n> ")
        if (c == 'y') or (c == 'Y'):
            del b
        else:
            break
