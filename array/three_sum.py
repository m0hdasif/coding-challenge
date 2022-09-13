# constraint -> all 3 indexes should be different
# Sol1: brute force- check elements sum is equal to target from i->0-n, j ->i+1-n, k->j+1-n
# T(n) = O(n^3)

from pair_two_sum import sorted_pair_sum_v2


# Sol2: use 2 sum to use the three_sum
# T(n)-> O(n)*O(nlogn) => O(n^2logn)
def three_sum(arr: list[int], target) -> list[int]:
    pairs = []
    for index, elem in enumerate(arr):
        two_sum_pairs = sorted_pair_sum_v2(arr[index + 1 :], target - elem)
        pairs.extend((elem, *two_sum_pair) for two_sum_pair in two_sum_pairs)
    return pairs


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4, 2, 5]
    target = 1
    print(three_sum(arr, target))
