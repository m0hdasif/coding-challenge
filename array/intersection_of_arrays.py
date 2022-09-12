def get_intersection(nums1: list[int], nums2: list[int]) -> list[int]:
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


if __name__ == "__main__":
    arr1 = [1, 2, 2, 2, 3, 4]
    arr2 = [2, 2, 3, 3]
    common_elements = get_intersection(arr1, arr2)
    print(common_elements)  # noqa
