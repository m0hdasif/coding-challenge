# https://leetcode.com/problems/complement-of-base-10-integer/


def bitwise_complement_by_shift_left(n: int) -> int:
    if n == 0:
        return 1
    shifting_key = 1
    # perform until shifting_key shift till max digit of n
    while shifting_key <= n:
        n ^= shifting_key
        shifting_key <<= 1
    return n


def bitwise_complement_by_comparing_each_binary_digit(n: int) -> int:
    if n == 0:
        return 1
    complement = 0
    i = 1
    while n:
        n, remainder = divmod(n, 2)
        complement += (not remainder) * i
        i *= 2
    return complement


# Solution by Code help(https://youtu.be/0fwrMYPcGQ0)
class Solution:
    def bitwise_complement_by_or_operator(self, n: int) -> int:
        return ~n & self.get_mask_with_1s(n)  #

    def get_mask_with_1s(self, n: int) -> int:
        mask = 0
        while n:
            mask = (mask << 1) | 1
            n >>= 1
        return mask


if __name__ == "__main__":
    val = 756
    print(f"{bitwise_complement_by_shift_left(val)=}")
    print(f"{bitwise_complement_by_comparing_each_binary_digit(val)=}")
    print(f"{Solution().bitwise_complement_by_or_operator(val)=}")
