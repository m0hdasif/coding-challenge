def check_palindrome(text: str) -> bool:
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and check_palindrome(text[1:-1])


if __name__ == "__main__":
    print(f'{check_palindrome("abdcdba")=}')
    print(f'{check_palindrome("abcdba")=}')
