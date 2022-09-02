#  Triangle is valid if sum of 2 sides is greater than other side


def is_valid_triangle(s1, s2, s3):
    sides = [s1, s2, s3]
    return all(
        side < sides[(index + 1) % 3] + sides[(index + 2) % 3]
        for index, side in enumerate(sides)
    )


a, b, c = [float(i) for i in input("Triangle sides: ").split()]

print(f"Triangle is valid: {is_valid_triangle(a, b, c)}")  # noqa
