# https://leetcode.com/problems/count-primes/
from math import ceil, sqrt

from is_prime import is_prime


# T(n) = O(n sqrt(n))
# S(n) = O(1)
def get_prime_nos_v1(n: int) -> int:
    return sum(is_prime(i) for i in range(2, n))


# T(n) = O(nlog(sqrtn))
# S(n) = O(log(n))
def get_prime_nos_v2(n: int) -> int:
    result = []
    for i in range(2, n):
        if all(
            i % prime_no != 0 for prime_no in result[: ceil(sqrt(len(result)))]
        ):
            result.append(i)
    return len(result)


# Sieve of Eratosthenes method
# T(n) = O(nlog(logn))
def get_prime_nos_v3(n: int) -> int:
    prime_nos = [True] * (n + 1)
    prime_nos[0] = prime_nos[1] = False
    count = 0
    for i in range(2, n):
        if prime_nos[i]:
            count += 1
            for j in range(2 * i, n, i):
                prime_nos[j] = False
    return count


if __name__ == "__main__":
    n = 10**4
    print(f"{get_prime_nos_v3(n)}")
    print(f"{get_prime_nos_v2(n)}")
    print(f"{get_prime_nos_v1(n)}")
