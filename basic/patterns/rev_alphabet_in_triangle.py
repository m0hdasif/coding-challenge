# Print the below pattern
# D
# C D
# B C D
# A B C D

# NOTE: chr changes char to int
# NOTE: ord changes char to int representing unicode code


def rev_alphabet_in_lower_triangle(n: int):
    for row in range(1, n + 1):
        start_val = n - row + 65  # 'A' = 65
        for col in range(row):
            val = chr(col + start_val)
            print(val, end=" ")
        print()


if __name__ == "__main__":
    rev_alphabet_in_lower_triangle(4)
