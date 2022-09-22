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


if __name__ == "__main__":
    text = "lorem aba abc daababc daabcbaabcbc abcbcabc"
    substring = "abc"
    print(remove_all_occurrences(text, substring))
