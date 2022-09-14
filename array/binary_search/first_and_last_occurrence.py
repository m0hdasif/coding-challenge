# Using binary search to find the first and last occurrence of the given match

# T(n)= O(logn)
def find_first_occurrence(arr: list[int], element: int) -> int:
    start = 0
    end = len(arr) - 1
    first_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == element:
            first_index = mid
            end = mid - 1
        elif arr[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return first_index


# T(n)= O(logn)
def find_last_occurrence(arr: list[int], element: int) -> int:
    start = 0
    end = len(arr) - 1
    last_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == element:
            last_index = mid
            start = mid + 1
        elif arr[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return last_index


def total_occurrences(arr: list[int], element: int) -> int:
    first_index = find_first_occurrence(arr, element)
    last_index = find_last_occurrence(arr, element)
    return last_index - first_index + 1 if first_index > 0 else 0


if __name__ == "__main__":
    arr = [1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
    el = 4
    print(f"{find_first_occurrence(arr, el)=}")
    print(f"{find_last_occurrence(arr, el)=}")
    print(f"{total_occurrences(arr, el)=}")
