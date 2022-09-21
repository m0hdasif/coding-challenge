def move_zeroes_to_right(nums: list[int]):
    zero_index = 0
    for elem_index, cur_val in enumerate(nums):
        # swap only if one is zero and other value.Once swapped, go to next element
        if cur_val:
            if not nums[zero_index]:
                nums[zero_index], nums[elem_index] = (
                    nums[elem_index],
                    nums[zero_index],
                )
            zero_index += 1


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 3, 12, 0, 0, 4, 0]
    move_zeroes_to_right(nums)
    print(nums)
