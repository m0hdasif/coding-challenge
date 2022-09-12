# get the common elements from 2 sorted arrays and it will all common elements, no matter how many times they are repeated

# sol1 : using 2 indexes
from collections import Counter


# T(n) =O(n+m), S(n)=O(1)
def intersection_by_2_pointers(nums1: list[int], nums2: list[int]) -> list[int]:
    index1 = 0
    index2 = 0
    common_elements = []
    while index1 < len(nums1) and index2 < len(nums2):
        elem1 = nums1[index1]
        elem2 = nums2[index2]
        if elem1 < elem2:
            index1 += 1
        elif elem1 > elem2:
            index2 += 1
        else:
            common_elements.append(elem1)
            index1 += 1
            index2 += 1
    return common_elements


# T(n) = O(max(m,n))
# S(n) = S(n) in worst case
def intersection_by_counter(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    val_counter = Counter(nums1)
    for elem2 in nums2:
        if elem2 in val_counter and val_counter[elem2] > 0:
            val_counter[elem2] -= 1
            res.append(elem2)

    return res


if __name__ == "__main__":
    arr1 = [1, 2, 2, 2, 3, 4]
    arr2 = [2, 2, 3, 3]
    print(  # noqa
        f"{intersection_by_2_pointers(arr1, arr2)=}"
    )  # output => [2, 2, 3]
    print(  # noqa
        f"{intersection_by_counter(arr1, arr2)=}"
    )  # output => [2, 2, 3]
