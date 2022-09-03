# Print the pattern in below format
# 1
# 2 3
# 4 5 6
# 7 8 9 10


def num_to_n_in_triangle_by_formula(n: int):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            val = row * (row - 1) // 2 + col
            print(val, end=" ")
        print()


def num_to_n_in_triangle_by_increment(n: int):
    val = 0
    for row in range(n):
        for _ in range(row + 1):
            val += 1
            print(val, end=" ")
        print()


if __name__ == "__main__":
    print("using row and column formula")
    num_to_n_in_triangle_by_formula(4)
    print("pattern by increment")
    num_to_n_in_triangle_by_increment(4)
