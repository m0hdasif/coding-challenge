from collections import Counter


def is_permutation_exist(string: str, element: str) -> bool:
    elements = Counter(element.lower())
    string = string.lower()
    elem_length = len(elements)
    current_set = string[:elem_length]  # start with 1st set in the loop
    letter_counts = dict(Counter(current_set))
    if is_char_counts_equal(elements, letter_counts):
        return True
    for index in range(len(string) - elem_length):
        set_last_char = string[elem_length + index]
        prev_set_last_char = string[index]
        letter_counts[set_last_char] = (
            letter_counts[set_last_char] + 1
            if set_last_char in letter_counts
            else 1
        )
        letter_counts[prev_set_last_char] = (
            letter_counts[prev_set_last_char] - 1
        )
        if is_char_counts_equal(elements, letter_counts):
            return True
    return False


def is_char_counts_equal(counter1: dict, counter2: dict):
    return all(value == counter2.get(el) for el, value in counter1.items())


if __name__ == "__main__":
    print(f'{is_permutation_exist("dabedaababc", "bac")=}')
