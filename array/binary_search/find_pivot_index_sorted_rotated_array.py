# pivot is the index from where sorted array should start(i.e minimum value)


def find_pivot_index(arr: list[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
    return (
        start if arr[start] < arr[0] else 0
    )  # to handle case where arr is not rotated


if __name__ == "__main__":
    arr = [7, 9, -3, -1, -1, 0, 1, 1, 3, 3, 4, 4, 7]
    print(find_pivot_index(arr))
