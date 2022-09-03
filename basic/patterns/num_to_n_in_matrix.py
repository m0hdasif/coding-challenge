# Print the pattern in below format
# 1 2 3
# 4 5 6
# 7 8 9


def num_to_n_in_matrix_by_formula(n: int):
    for row in range(n):
        for col in range(1, n + 1):
            print(row * n + col, end=" ")
        print()


def num_to_n_in_matrix_by_increment(n: int):
    val = 0
    for _ in range(1, n + 1):
        for _ in range(1, n + 1):
            val += 1
            print(val, end=" ")
        print()


if __name__ == "__main__":
    print("using row and column formula")
    num_to_n_in_matrix_by_formula(3)
    print("pattern by increment")
    num_to_n_in_matrix_by_increment(3)
