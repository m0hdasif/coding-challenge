def reverse_string(text: str) -> str:
    return text if len(text) <= 1 else reverse_string(text[1:]) + text[0]


if __name__ == "__main__":
    print(reverse_string("asif"))
