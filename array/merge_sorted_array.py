# https://leetcode.com/problems/merge-sorted-array/
# S(n) = O(1)
# T(n) = O(n)
def merge_sorted_array_with_dynamic_length(
    nums1: list[int], nums2: list[int]
) -> None:
    n1 = 0
    n2 = 0
    while n1 < len(nums1) and n2 < len(nums2):
        if nums1[n1] > nums2[n2] or nums1[n1] == 0:
            nums1.insert(n1, nums2[n2])
            nums1.pop()
            n2 += 1
        n1 += 1


# S(n) = O(1)
# T(n) = O(n^2)
def merge_sorted_array_with_fixed_length(
    nums1: list[int], nums2: list[int]
) -> None:
    n1 = 0
    n2 = 0
    while n1 < len(nums1) and n2 < len(nums2):
        if nums1[n1] > nums2[n2]:
            __rotate_array_to_given_index(nums1, n1)
            nums1[n1] = nums2[n2]
            n2 += 1
        elif nums1[n1] == 0:
            nums1[n1] = nums2[n2]
            n2 += 1
        n1 += 1


def __rotate_array_to_given_index(nums, index):
    i = len(nums) - 1
    while i > index:
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
        i -= 1


if __name__ == "__main__":

    def get_nums1():
        return [1, 2, 3, 4, 0, 0, 0, 0]

    nums1 = get_nums1()
    nums2 = [2, 3, 5, 6]
    merge_sorted_array_with_dynamic_length(nums1, nums2)
    print(nums1)
    nums1 = get_nums1()
    merge_sorted_array_with_fixed_length(nums1, nums2)
    print(nums1)
