def reverse_words_order(sentence: str) -> str:
    word = ""
    reverse_sentence = ""
    for char in sentence:
        if char in [" ", ",", "."]:
            reverse_sentence = f"{char}{word}{reverse_sentence}"
            word = ""
        else:
            word += char
    reverse_sentence = f"{word}{reverse_sentence}"
    return reverse_sentence


if __name__ == "__main__":
    sentence = "main taan sharaab chhadd doon, mainu nhi sharab chadd di."
    print(reverse_words_order(sentence))
