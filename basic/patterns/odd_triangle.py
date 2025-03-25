# Print the triangle in below format
# for n =5
#     *
#    ***
#   *****
#  *******
# *********

def triangle(n: int):
    for row in range(n):
        _print_space(row, n)
        _print_char(row, "*")


def _print_space(row: int, total_row: int):
    print(" " * (total_row - row - 1), end="")


def _print_char(row: int, character: str = "*"):
    print(character * (2 * row + 1))


if __name__ == "__main__":
    triangle(5)
