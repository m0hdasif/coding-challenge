# card like sorting, sort small block then keep sorting new element in each turn
# T(n) = O(n^2) for worst and average case and O(n) for best case
# Good for smaller arrays
def insertion_sort(arr: list[int]) -> list[int]:
    for index, _ in enumerate(arr):
        i = index
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

    return arr


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 1, 1, 2, 4, 6, 10, 8]
    print(f"{insertion_sort(arr)=}")
