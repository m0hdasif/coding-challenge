from search_elem import print_2d_list


def spiral_traversal(matrix: list[list[int]]) -> list[int]:
    min_row_index = 0
    min_col_index = 0
    max_row_index = len(matrix) - 1
    max_col_index = len(matrix[0]) - 1
    traversal = []
    total_elements = len(matrix[0]) * len(matrix)

    while min_row_index <= max_row_index and min_col_index <= max_col_index:
        # first row
        for col_index in range(min_col_index, max_col_index + 1):
            traversal.append(matrix[min_row_index][col_index])
        min_row_index += 1

        # last column
        traversal.extend(
            matrix[row_index][max_col_index]
            for row_index in range(min_row_index, max_row_index + 1)
        )
        print(
            "🐍 File: two_dimensional/spiral_print.py | Line: 17 | spiral_traversal ~ traversal",
            traversal,
        )
        max_col_index -= 1

        if len(traversal) >= total_elements:
            break
        # last row
        for col_index in range(max_col_index, min_col_index - 1, -1):
            traversal.append(matrix[max_row_index][col_index])
        max_row_index -= 1

        # first row
        traversal.extend(
            matrix[row_index][col_index]
            for row_index in range(max_row_index, min_row_index - 1, -1)
        )
        min_col_index += 1

        print(min_row_index, min_col_index, max_row_index, max_col_index)
    return traversal


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_2d_list(matrix)
    elements = spiral_traversal(matrix)
    print(elements)
