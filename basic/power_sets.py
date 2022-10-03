# Get all the possible sub sets of given sets
def power_sets(
    input_set: list[int], output: list[int] = None, index: int = 0
) -> list[list[int]]:
    if output is None:
        output = []
    set_list = []
    if index >= len(input_set):
        return [output]
    # exclude the indexed value
    set_list.extend(power_sets(input_set, output, index + 1))
    # include the indexed value
    set_list.extend(
        power_sets(input_set, output + [input_set[index]], index + 1)
    )
    return set_list


if __name__ == "__main__":
    print(f"{power_sets([1,2,3,4])=}")
