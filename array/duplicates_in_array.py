# https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/1506264/Python-or-Constant-Space-and-Linear-Timeor-Multiple-Solutions-With-Explanation
# find duplicates in an array where number can be 1 to n
# T(n) = O(n)
# S(n) = O(1)
def duplicates(nums: list[int]) -> list[int]:
    n = len(nums)
    nums = [num - 1 for num in nums]
    for num in nums:
        nums[num % n] += n
    # check how many times, then return if crossed more than once
    return [key + 1 for key, num in enumerate(nums) if num // n >= 2]


if __name__ == "__main__":
    print(duplicates([1, 4, 3, 4, 7, 6, 7, 4, 4, 8]))
