from math import sqrt


def is_prime(n: int):
    return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))


if __name__ == "__main__":
    print(is_prime(4))
