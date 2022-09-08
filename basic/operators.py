# Arithmetic operators
integer_div_value = 50 // 3
print("🐍 integer_div_value", integer_div_value)  # noqa
int_modulo = 50 % 3
print("🐍 int_modulo", int_modulo)  # noqa
# above equivalent
integer_div_value, int_modulo = divmod(50, 3)
print("🐍 integer_div_value", integer_div_value)  # noqa
print("🐍 int_modulo", int_modulo)  # noqa


# bitwise operators
print(1 | 2)  # 001 + 010 -> 011
print(~1)  # -ve 2's complement
print(5 ^ 7)  # xor -> 2
print(5 << 3)  # 5 x 2**3 => left shift
print(5 >> 2)  # int(5 / (2**2)) => right shift
