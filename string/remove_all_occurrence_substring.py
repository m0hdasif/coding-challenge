def remove_all_occurrences(string: str, substring: str):
    next_match_index = 0
    while next_match_index >= 0:
        next_match_index = string.find(substring, next_match_index)
        if next_match_index >= 0:
            string = (
                string[:next_match_index]
                + string[next_match_index + len(substring) :]
            )
    return string


def recursive_remove_all_occurrences(string: str, substring: str):
    prev_string = None
    updated_string = string
    while updated_string != prev_string:
        prev_string = updated_string
        updated_string = remove_all_occurrences(prev_string, substring)
    return updated_string


if __name__ == "__main__":
    text = "lorem aba abc daababc daabcbaabcbcabccabc"
    substring = "abc"
    print(remove_all_occurrences(text, substring))
    print(recursive_remove_all_occurrences(text, substring))
