# array of elements with 2 occurrence except 1 element
def get_unique_element(arr: list[int]) -> int:  # T(n) => O(n), S(n)=O(1)
    ans = 0
    for elem in arr:
        ans ^= elem  # apply xor twice on same element return 0
    return ans


def get_unique_element_from_sorted_array(
    arr: list[int], start=0, end=None
) -> int:  # T(n) => O(logn), S(n)=O(1)
    if end is None:
        end = len(arr) - 1
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    if arr[mid] == arr[mid + 1]:
        return get_unique_element_from_sorted_array(arr, start, mid - 1)
    return get_unique_element_from_sorted_array(arr, mid + 1, end)


if __name__ == "__main__":
    print(get_unique_element([1, 3, 4, 5, 4, 5, 1]))
    print(get_unique_element_from_sorted_array([1, 1, 4, 4, 5, 5, 6]))
