# T(n) = O(n^2) in all average, best and worst case
# S(n) = O(1)
# Use case: good for smaller lists
def selection_sort(arr: list[int]) -> list[int]:
    """Place the smallest element in the right slot in each pass."""
    # last element would be sorted already
    for index, _ in enumerate(arr[:-1]):
        min_elem_index = index
        for cur_index, cur_element in enumerate(arr[index:], start=index):
            if cur_element < arr[min_elem_index]:
                min_elem_index = cur_index
        arr[min_elem_index], arr[index] = arr[index], arr[min_elem_index]

    return arr


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 1, 2, 4, 10, 7, 6, 8, 9]
    print(f"{selection_sort(arr)}")
