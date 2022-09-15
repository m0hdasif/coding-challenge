# find the square root of the number N using BS
from math import sqrt


def find_sqrt_by_b_search(low, high, number, precision=1):
    if precision <= 0 or precision > 10:
        raise ValueError("precision must be within 1 to 10")
    # If the range is still valid
    if low <= high:

        # Find the mid-value of the range
        mid = (low + high) / 2

        # Base Case
        if (mid * mid == number) or abs(mid * mid - number) < (
            0.1
        ) ** precision:
            return mid

        # Condition to check if the
        # left search space is useless
        elif mid * mid < number:
            return find_sqrt_by_b_search(mid, high, number, precision)

        else:
            return find_sqrt_by_b_search(low, mid, number, precision)

    return low


# Driver Code
if __name__ == "__main__":

    n = 9223372036854
    print(find_sqrt_by_b_search(0, n, n, 10))
    print(sqrt(n))
