# https://leetcode.com/problems/find-the-duplicate-number/
# duplicate number can be repeated multiple times
def find_duplicate(nums: list[int]) -> int:
    slow, fast = nums[0], nums[0]
    # index of closed loop
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break

    # find element with same value in the closed loop
    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow


if __name__ == "__main__":
    print(find_duplicate([3, 1, 9, 2, 5, 4, 6, 3, 7, 8]))
