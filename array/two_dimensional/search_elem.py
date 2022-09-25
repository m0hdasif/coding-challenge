def input_2d_list(rows, cols) -> list[list[int]]:
    matrix: list[list[int]] = get_default_2d_list(rows, cols)
    for row in range(rows):
        values = input(f"Row {row+1}: ").split()
        if len(values) != cols:
            raise ValueError(f"Number of columns must be equal to {cols}")
        matrix[row] = [int(v) for v in values]
    return matrix


def get_default_2d_list(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_2d_list(matrix: list[list[int]]) -> None:
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def find_element(matrix: list[list[int]], element: int) -> int:
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col == element:
                return (row_index, col_index)
    return (-1, -1)


if __name__ == "__main__":
    rows, cols = (int(i) for i in input("Enter rows and columns: ").split())
    arr = input_2d_list(rows, cols)
    print("Entered Matrix")
    print_2d_list(arr)
    element = int(input("Enter element to search: "))
    found_index = find_element(arr, element)
    if found_index == (-1, -1):
        print("Element not found.")
    else:
        print(f"Element found at {found_index}")
