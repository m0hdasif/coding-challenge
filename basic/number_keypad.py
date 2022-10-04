def get_chars(num: int) -> list[chr]:
    if not (2 <= num <= 9):
        return []
    no_of_element = 4 if num in {7, 9} else 3
    offset = num > 7  # to increment the counter after 7
    return [chr(97 + (num - 2) * 3 + i + offset) for i in range(no_of_element)]


# T(n) = O(3^n) # 3*(3**n)
def get_possible_text(nums: str) -> list[str]:
    values = [""]
    for num in nums:
        chars = get_chars(int(num))
        new_values = []
        for char in chars:
            new_values.extend(val + char for val in values)
        values = new_values
    return values


if __name__ == "__main__":
    print(get_possible_text("2743"))
