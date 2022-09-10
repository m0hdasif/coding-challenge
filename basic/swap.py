def swap_with_xor(a: int, b: int) -> int:
    a ^= b
    b ^= a  # b = a^(b^b) => b = a^0 => a
    a ^= b  # a = (a^a)^b => a = b^0 => b
    return a, b


if __name__ == "__main__":
    print(swap_with_xor(2, 5))
