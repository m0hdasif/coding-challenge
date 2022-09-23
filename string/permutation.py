from itertools import permutations


def builtin_permutations(string: str) -> list[str]:
    return ["".join(el) for el in permutations(string)]


def get_permutation(string: str) -> list[str]:
    results = []
    chars = list(string)
    if len(chars) == 1:
        return [chars[0]]
    for index in range(len(chars)):
        # chars before index value
        initial_chars = chars[:index] if index > 0 else []
        # get permutation for the remaining chars except index value
        sub_permutations = get_permutation(initial_chars + chars[index + 1 :])
        # append both permutations and values
        results.extend([chars[index] + p for p in sub_permutations])

    return results


if __name__ == "__main__":
    val = "yum"
    print(builtin_permutations(val))
    print(get_permutation(val))
