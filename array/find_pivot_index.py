# pivot is the index where sum of left and right elements are equal.


def find_pivot_index(arr: list[int]) -> int:
    left = 0
    right = sum(arr)
    for index, cur_element in enumerate(arr):
        right -= cur_element
        if index:
            left += arr[index - 1]
        if left == right:
            return index

    return -1


if __name__ == "__main__":
    arr = [1, 3, -3, 1, 5, 4, 0, -1, -1]
    print(find_pivot_index(arr))  # return 4 index
