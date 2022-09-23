# https://leetcode.com/problems/string-compression/


def compress_string(chars: list[chr]) -> tuple[list[chr], int]:
    index = 0
    compressed_length = 0
    while index < len(chars):
        next_different_elem_index = index + 1
        while (
            next_different_elem_index < len(chars)
            and chars[index] == chars[next_different_elem_index]
        ):
            next_different_elem_index += 1
        chars[compressed_length] = chars[index]
        compressed_length += 1

        if next_different_elem_index - index > 1:
            # for changing count > single digit to separate chars
            for cnt in list(str(next_different_elem_index - index)):
                chars[compressed_length] = cnt
                compressed_length += 1

        index = next_different_elem_index
    return list(chars), compressed_length


if __name__ == "__main__":
    text = list("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccddeffff")
    compressed_text_in_line_replaced, length = compress_string(text)
    print(
        f"Inline compressed value: {compressed_text_in_line_replaced} with length:{length}"
    )
    final_compressed_char_list = compressed_text_in_line_replaced[:length]
    print(f"{final_compressed_char_list=}")
