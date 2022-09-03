# Print the below pattern
# A B C
# B C D
# E F G


def alphabets_in_matrix(n: int):
    for row in range(n):
        for col in range(row, row + n):
            val = chr(col + 65)  # 'A' = 65
            print(val, end=" ")
        print()


if __name__ == "__main__":
    alphabets_in_matrix(14)
