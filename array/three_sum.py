# constraint -> all 3 indexes should be different
from pair_two_sum import sorted_pair_sum_v2

# Sol1: brute force- check elements sum is equal to target from i->0-n, j ->i+1-n, k->j+1-n
# T(n) = O(n^3)
# S(n) = O(1)


# Sol2: use 2 sum to use the three_sum
# T(n)-> O(n)*O(nlogn) => O(n^2logn)
# S(n) = O(1)


def three_sum(arr: list[int], target) -> list[int]:
    pairs = []
    for index, elem in enumerate(arr):
        two_sum_pairs = sorted_pair_sum_v2(arr[index + 1 :], target - elem)
        pairs.extend((elem, *two_sum_pair) for two_sum_pair in two_sum_pairs)
    return pairs


# Sol3: use the above solution to sort first then iterate over the loop and find the two sum pairs
# T(n): O(n^2) # [O(nlogn) +O(n^2)]
# S(n): O(1)

# Sol4 : using 3 pointers -> basic logic is similar to above(https://www.code-recipe.com/post/three-sum)
# T(n): O(n^2) # [O(nlogn) +O(n^2)]
# S(n): O(1)
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4, 2, 5]
    target = 1
    print(three_sum(arr, target))
