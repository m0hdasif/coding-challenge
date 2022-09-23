def find_substring(
    string: str, substring: str, start: int = 0, end: int = None
):
    if end is None:
        end = len(string)
    for index, _ in enumerate(string[start:end]):
        i = index
        while string[start + i] == substring[i - index]:
            i += 1
            if i - index == len(substring):
                return start + index
    return -1


if __name__ == "__main__":
    text = "lorem aba abc daababc daabcbaabcbc abcbcabc"
    substring = "abc"
    print(find_substring(text, substring))
