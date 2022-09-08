# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
class HammingWeight:
    def get_hamming_weight_binary_conversion(
        self, n: int
    ) -> int:  # 1 million times took 1.97seconds
        total_one = 0
        while n:
            n, remainder = divmod(n, 2)
            total_one += remainder
        return total_one

    def get_hamming_weight_by_bitwise_and(
        self, n: int
    ) -> int:  # 1 million times took 0.97seconds
        """Remove the last set bit from the number and execute only set bits times."""
        total_one = 0
        while n:
            n &= n - 1
            total_one += 1
        return total_one

    def get_hamming_weight_by_right_shift(
        self, n: int
    ) -> int:  # 1 million times took 1.85seconds
        """Solution by code help(https://youtu.be/yjdQHb2elqI)."""
        total_one = 0
        while n:
            if n & 1:
                total_one += 1
            n >>= 1
        return total_one


if __name__ == "__main__":
    answer = HammingWeight().get_hamming_weight_binary_conversion(31)  # 5 times
    print(f"binary conversion {answer=}")  # 5
    answer = HammingWeight().get_hamming_weight_by_bitwise_and(31)  # 5 times
    print(f"bit-wise and operator {answer=}")  # 5
    answer = HammingWeight().get_hamming_weight_binary_conversion(32)  # 6 times
    print(f"binary conversion {answer=}")  # 1
    answer = HammingWeight().get_hamming_weight_by_bitwise_and(32)  # 1 time
    print(f"bit-wise and operator {answer=}")  # 1
    answer = HammingWeight().get_hamming_weight_by_right_shift(32)  # 6 times
    print(f"right shift operator {answer=}")  # 1
