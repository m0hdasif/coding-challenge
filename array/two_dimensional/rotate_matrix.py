# https://leetcode.com/problems/rotate-image/
# rotate clockwise by 90 degrees
# 1 2 3     7 4 1
# 4 5 6  -> 8 5 2
# 7 8 9     9 6 3
from search_elem import print_2d_list


def rotate_matrix(matrix):
    for row_index in range(len(matrix) // 2):
        row_len = len(matrix[row_index])
        for col_index in range(row_index, row_len - 1 - row_index):
            temp = matrix[row_index][col_index]
            matrix[row_index][col_index] = matrix[row_len - 1 - col_index][
                row_index
            ]
            matrix[row_len - 1 - col_index][row_index] = matrix[
                row_len - 1 - row_index
            ][row_len - 1 - col_index]
            matrix[row_len - 1 - row_index][row_len - 1 - col_index] = matrix[
                col_index
            ][row_len - 1 - row_index]
            matrix[col_index][row_len - 1 - row_index] = temp


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, "a"],
        [4, 5, 6, "b"],
        [7, 8, 9, "c"],
        ["d", "e", "f", "g"],
    ]
    print("Before rotation:")
    print_2d_list(matrix)
    rotate_matrix(matrix)
    print("After rotation:")
    print_2d_list(matrix)
