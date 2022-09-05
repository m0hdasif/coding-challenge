# Print patterns in below format
#       1
#     2 3
#   4 5 6
# 7 8 9 10


def num_in_lower_right_triangle_by_increment(n: int):
    val = 0
    for row in range(1, n + 1):
        for _ in range(n - row):
            print(" ", end=" ")
        for _ in range(row):
            val += 1
            print(val, end=" ")
        print()


def num_in_lower_right_triangle_by_formula(n: int):
    for row in range(1, n + 1):
        for _ in range(n - row):
            print(" ", end=" ")
        for col in range(1, row + 1):
            val = row * (row - 1) // 2 + col
            print(val, end=" ")
        print()


if __name__ == "__main__":
    row_count = 4
    print("By increment")
    num_in_lower_right_triangle_by_increment(row_count)
    print("By formula")
    num_in_lower_right_triangle_by_formula(row_count)
