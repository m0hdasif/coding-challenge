def quicksort(arr, start=0, end=None):
    if not end:
        end = len(arr) - 1

    if start >= end:
        return arr
    p = partition(arr, start, end)
    if start <= p <= end:
        quicksort(arr, start, p - 1)
        quicksort(arr, p + 1, end)
    return arr


def partition(arr, start, end):
    chosen_random_index = start
    pivot_index = sum(el < arr[chosen_random_index] for el in arr)
    arr[chosen_random_index], arr[pivot_index] = (
        arr[pivot_index],
        arr[chosen_random_index],
    )
    i = start
    j = end
    while i < pivot_index and j > pivot_index:
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] <= arr[pivot_index]:
            i += 1
        if arr[j] >= arr[pivot_index]:
            j -= 1
    return pivot_index


if __name__ == "__main__":
    arr = [5, 3, 1, 7, 4, 1, 2, 4, 10, 1, 6, 8, 9]
    print(f"{quicksort(arr)=}")
