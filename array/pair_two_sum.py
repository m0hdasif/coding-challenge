def pair_sum(nums: list[int], target: int) -> list[int]:
    complement_value_map = {}
    pairs = []
    for value in nums:
        complement_value = complement_value_map.get(value)
        if complement_value is not None:
            pairs.append((complement_value, value))
        complement_value_map[target - value] = value
    return pairs


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 5, 8, 9]
    target = 9
    print(f"{pair_sum(arr,9)=}")
