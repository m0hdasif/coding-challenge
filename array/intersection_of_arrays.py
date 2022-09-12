# find intersection of 2 unsorted arrays and return unique values
# Sol1
# T(n)=O(max(n,m)), making set from list, then O(min(n,m)) for intersection
# S(n) = O(max(n,m)), making set from list
from collections import Counter


def intersection_by_set(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


# Sol2:
# sort the list and use the array.intersection_of_sorted_arrays.intersection_by_2_pointers to find the intersection
# T(n)=O(nlog(n)) for sorting the array, and intersection can be found in O(m+n)

# Sol3:
# brute force, going through each element and check if exists in both lists
# T(n) => O(m*n)

# Sol4:
# T(n) = O(max(m,n))
# S(n) = S(n) in worst case
def intersection_by_counter(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    val_counter = Counter(nums1)
    for elem2 in nums2:
        if elem2 in val_counter:
            val_counter.pop(elem2)
            res.append(elem2)

    return res


if __name__ == "__main__":
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(f"{intersection_by_set(arr1,arr2)=}")  # noqa /return [2]
    print(f"{intersection_by_counter(arr1,arr2)=}")  # noqa /return [2]
