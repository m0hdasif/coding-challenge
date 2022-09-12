# array of elements with 2 occurrence except 1 element
def get_unique_element(arr: list[int]) -> int:  # T(n) => O(n), S(n)=O(1)
    ans = 0
    for elem in arr:
        ans ^= elem  # apply xor twice on same element return 0
    return ans


if __name__ == "__main__":
    print(get_unique_element([1, 3, 4, 5, 4, 5, 1]))  #
