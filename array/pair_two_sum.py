# T(n) =O(n), S(n)=O(n)
# TODO: fix issue with inconsistent multiple elements for repeated values
def pair_sum(nums: list[int], target: int) -> list[int]:
    complement_value_map = {}
    pairs = []
    for value in nums:
        complement_value = complement_value_map.get(value)
        if complement_value is not None:
            pairs.append((complement_value, value))
        complement_value_map[target - value] = value
    return pairs


# T(n) = O(nlogn) for sorting, S(n)=O(1)
# method using 2 pointers to lists
def sorted_pair_sum_v2(nums: list[int], target: int) -> list[int]:
    nums.sort()
    start_index = 0
    end_index = max(0, len(nums) - 1)
    pairs = []
    while start_index < end_index:
        sum_val = nums[start_index] + nums[end_index]
        if sum_val == target:
            pairs.append((nums[start_index], nums[end_index]))
            start_index += 1
        elif sum_val > target:
            end_index -= 1
        else:
            start_index += 1

    return pairs


def unique_pair_sum(nums: list[int], target: int) -> list[int]:
    return list(set(pair_sum(nums, target)))


# T(n)= O(nlogn) for sorting
def sorted_unique_pair_sum(nums: list[int], target: int) -> list[int]:
    unique_pairs = unique_pair_sum(nums, target)
    unique_pairs.sort(key=lambda x: x[0])
    return unique_pairs


# T(n)= O(nlogn) for sorting
# S(n) = O(n) for worst case
def sorted_unique_pair_sum_v2(nums: list[int], target: int) -> list[int]:
    complement_value_map = {}
    pairs = []
    for value in nums:
        complement_value = complement_value_map.get(value)
        if complement_value is not None:
            pairs.append((complement_value, value))
            complement_value_map.pop(value)
        complement_value_map[target - value] = value
    pairs.sort(key=lambda x: x[0])
    return pairs


if __name__ == "__main__":
    arr = [1, 2, 3, 6, 4, 6, 5, 8, 9]
    target = 9
    print(f"{pair_sum(arr,target)=}")  # 4 elements
    print(f"{sorted_pair_sum_v2(arr,target)=}")
    print(f"{sorted_unique_pair_sum(arr,target)=}")
    print(f"{sorted_unique_pair_sum_v2(arr,target)=}")
