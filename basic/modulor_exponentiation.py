# https://www.codingninjas.com/codestudio/problems/modular-exponentiation_1082146

# ! Slower implementation for big numbers
def modular_exponentiation_v1(base: int, exponent: int, divisor: int) -> int:
    power_val = get_power_value(base, exponent)
    return power_val % divisor


# T(n) = O(log(n)), S(n)=O(1)
def get_power_value(base: int, exponent: int):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    value = get_power_value(base, exponent // 2)
    return value * value if exponent % 2 == 0 else base * value * value


# * (a*b)%m = (a%m)*(b%m)
# * a%m = (a%m)%m
# ! Faster approach as it takes less time to multiply smaller numbers
def modular_exponentiation_v2(base: int, exponent: int, divisor: int) -> int:
    if exponent == 0:
        return 1 if divisor > 1 else 0
    if exponent == 1:
        return base % divisor
    val = modular_exponentiation_v2(base, exponent // 2, divisor)
    return (
        (base * val * val) % divisor
        if exponent & 1  # ? is odd
        else (val * val) % divisor
    )


if __name__ == "__main__":
    x = 10**8 - 1
    n = 10**6 + 1
    m = 10
    print(f"{modular_exponentiation_v2(x, n, m)=}")
    print(f"{modular_exponentiation_v1(x, n, m)=}")
