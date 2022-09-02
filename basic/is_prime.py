from math import sqrt


def is_prime(n: int):
    return not any((n % i == 0) for i in range(2, int(sqrt(n))))
