def binary_search_matrix(
    matrix: list[list[int]], target: int
) -> tuple[int, int]:
    start_row_index = 0
    last_row_index = len(matrix) - 1
    found_row_index = 0

    while start_row_index < last_row_index:
        mid = (start_row_index + last_row_index) // 2
        if target < matrix[mid][0]:
            last_row_index = mid - 1
            found_row_index = last_row_index
        elif target <= matrix[mid][len(matrix[mid]) - 1]:
            last_row_index = mid
            start_row_index = mid
            found_row_index = mid
        else:
            start_row_index = mid + 1
            found_row_index = start_row_index

    if found_row_index >= len(matrix) or found_row_index < 0:
        return -1, -1

    start_col_index = 0
    last_col_index = len(matrix[found_row_index]) - 1
    while start_col_index <= last_col_index:
        mid = (start_col_index + last_col_index) // 2
        if target == matrix[found_row_index][mid]:
            return found_row_index, mid
        elif target > matrix[found_row_index][mid]:
            start_col_index = mid + 1
        else:
            last_col_index = mid - 1
    return -1, -1


def binary_search_matrix_v2(
    matrix: list[list[int]], target: int
) -> tuple[int, int]:
    start = 0
    end = len(matrix) * len(matrix[0]) - 1
    while start <= end:
        mid = start + (end - start) // 2
        row_index, col_index = divmod(mid, len(matrix[0]))
        element = matrix[row_index][col_index]
        if element == target:
            return row_index, col_index

        if element < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1, -1


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = 5
    print(binary_search_matrix(matrix, target))
    print(binary_search_matrix_v2(matrix, target))
