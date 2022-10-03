# T(n) = O(n^2) in average and worst case, O(n) in best case

# S(n) = O(1)
# Use case: place ith largest number at its correct position
def bubble_sort(arr: list[int]) -> list[int]:
    """Sort adjacent elements in each pass until sorted."""
    for sorted_element_count, _ in enumerate(arr, start=1):
        is_sorted = True
        for cur_index in range(len(arr) - sorted_element_count):
            if arr[cur_index] > arr[cur_index + 1]:
                arr[cur_index], arr[cur_index + 1] = (
                    arr[cur_index + 1],
                    arr[cur_index],
                )
                is_sorted = False  # if any element swapped then not sorted
        if is_sorted:
            break

    return arr


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 1, 2, 4, 10, 7, 6, 8, 9]
    print(f"{bubble_sort(arr)=}")
