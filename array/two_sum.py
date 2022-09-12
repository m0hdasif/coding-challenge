# sol1: brute force -> compare each number with each number in the list and sum == given given sum
# T(n) = O(n^2), S(n)=O(1)

# Sol2: dict of required value as key and number as value
def two_sum_with_dict(nums: list[int], target: int) -> tuple[int, int]:

    target_index_map = {target - num: index for index, num in enumerate(nums)}
    return next(
        (
            (index, target_index_map[num])
            for index, num in enumerate(nums)
            if target_index_map.get(num) is not None
            and index != target_index_map[num]
        ),
        None,
    )


# sol3: dict with single loop
def two_sum_with_dict_v2(nums: list[int], target: int) -> tuple[int, int]:
    target_index_map = {}
    for index, cur_val in enumerate(nums):
        matched_index = target_index_map.get(target - cur_val)
        if matched_index is not None:
            return matched_index, index
        target_index_map[cur_val] = index


if __name__ == "__main__":
    arr = [3, 2, 4]  # [2,7,11,15,4,8]
    target = 6  # 9
    print(two_sum_with_dict(arr, target))
    print(two_sum_with_dict_v2(arr, target))
