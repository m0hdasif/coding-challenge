# T(n)= O(logn)
def binary_search_in_sorted_rotated_array(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target and (
            arr[len(arr) - 1] > target or arr[mid] >= arr[0]
        ):
            start = mid + 1
        else:
            end = mid - 1
    return -1


# T(n)= O(logn)
def binary_search_in_sorted_rotated_array_v2(
    arr: list[int], target: int
) -> int:
    from binary_search import b_search
    from find_pivot_index_sorted_rotated_array import find_pivot_index

    pivot = find_pivot_index(arr)  # to get 2 sorted arrays
    # find the element within one of sorted arrays
    if arr[pivot] == target:
        return pivot
    elif arr[pivot] < target <= arr[len(arr) - 1]:
        return b_search(arr, target, pivot, len(arr) - 1)
    else:
        return b_search(arr, target, 0, pivot - 1)


if __name__ == "__main__":
    arr = [7, 9, -3, -1, -1, 0, 1, 1, 3, 3, 4, 4, 7]
    target = 4
    print(f"{binary_search_in_sorted_rotated_array(arr, target)=}")
    print(f"{binary_search_in_sorted_rotated_array_v2(arr, target)=}")
