# Print below patterns
# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 @ @ 4 3 2 1
# 1 2 3 @ @ @ @ 3 2 1
# 1 2 @ @ @ @ @ @ 2 1
# 1 @ @ @ @ @ @ @ @ 1
# @ @ @ @ @ @ @ @ @ @
# 1 @ @ @ @ @ @ @ @ 1
# 1 2 @ @ @ @ @ @ 2 1
# 1 2 3 @ @ @ @ 3 2 1
# 1 2 3 4 @ @ 4 3 2 1
# 1 2 3 4 5 5 4 3 2 1


def print_combine_pattern(total_n_count, special_char="@"):

    for row in range(total_n_count, 0, -1):
        print_single_row(total_n_count, row, special_char)

    print_single_row(total_n_count, 0, special_char)
    for row in range(1, total_n_count + 1):
        print_single_row(total_n_count, row, special_char)


def print_single_row(total_n_count, row, special_char):
    print_number_list(row)
    print_character_n_times(2 * (total_n_count - row), special_char)
    print_reversed_number_list(row)
    print()


def print_number_list(n):
    for i in range(1, n + 1):
        print(i, end=" ")


def print_reversed_number_list(n):
    for i in range(
        n, 0, -1
    ):  # it will go from n to 1 like n= 5,=> i = 5 4 3 2 1
        print(i, end=" ")


def print_character_n_times(n, char):
    for _ in range(n):
        print(char, end=" ")


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_combine_pattern(n)
