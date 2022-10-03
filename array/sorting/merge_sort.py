# S(n) = O(n) for max array
# T(n) = O(nlog(n))
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    start = merge_sort(arr[: len(arr) // 2])
    end = merge_sort(arr[len(arr) // 2 :])
    return merge(start, end)


def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 1, 2, 4, 10, 7, 6, 8, 9]
    print(f"{merge_sort(arr)=}")
