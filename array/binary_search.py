# Search an element in the sorted array and return its index if found else return -1
def binary_search_by_recursion(arr: list[int], target: int) -> int:
    return b_search(arr, target, 0, len(arr) - 1)


def b_search(arr: list[int], target: int, start: int, end: int) -> int:
    if start > end:
        return -1
    mid = start + (end - start) // 2  # start+end//2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return b_search(arr, target, start, mid - 1)
    return b_search(arr, target, mid + 1, end)


def binary_search_by_iteration(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 9, 16, 17, 18, 29, 30]
    target = 18
    print(f"{binary_search_by_recursion(arr, target)=}")
    print(f"{binary_search_by_iteration(arr, target)=}")
