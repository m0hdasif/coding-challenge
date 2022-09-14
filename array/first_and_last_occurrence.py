# Using binary search to find the first and last occurrence of the given match


def find_first_occurrence(arr: list[int], element: int) -> list[int]:
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


def find_last_occurrence(arr: list[int], element: int) -> list[int]:
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


if __name__ == "__main__":
    arr = [1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
    el = 4
    print(f"{find_first_occurrence(arr, el)=}")
    print(f"{find_last_occurrence(arr, el)=}")
