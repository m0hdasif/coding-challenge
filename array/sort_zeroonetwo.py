# Sol1:
# T(n) = O(n)
# S(n) = O(1)
# count all numbers and then first zero then 1 then 2
def sort_012_using_counter(arr: list[int]) -> list[int]:
    from collections import Counter

    counter = Counter(arr)
    return [0] * counter[0] + [1] * counter[1] + [2] * counter[2]


# by maintaining 3 pointers
def sort_012_by_pointer(arr: list[int]) -> list[int]:
    sorted_arr = arr.copy()
    zero_index = 0
    one_index = 0
    two_index = len(sorted_arr) - 1
    while one_index <= two_index:
        if sorted_arr[one_index] == 0:
            sorted_arr[one_index] = sorted_arr[zero_index]
            sorted_arr[zero_index] = 0
            zero_index += 1
            one_index += 1
        elif sorted_arr[one_index] == 1:
            one_index += 1
        else:
            sorted_arr[one_index] = sorted_arr[two_index]
            sorted_arr[two_index] = 2
            two_index -= 1
    return sorted_arr


if __name__ == "__main__":
    arr = [1, 0, 2, 1, 2, 1, 2, 2, 1, 2, 0, 2, 1, 0]
    print(sort_012_using_counter(arr))
    print(sort_012_by_pointer(arr))
