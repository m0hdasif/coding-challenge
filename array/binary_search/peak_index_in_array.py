# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# it will return index of peak value and min elements in array ==3
def find_peak_index(arr: list[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] >= arr[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return mid


# does not work with same repeated numbers
def find_peak_index_v2(arr: list[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == "__main__":
    print(
        f"{find_peak_index([1,2,3,3,3,4,2,0])=}"
    )  # should return 5 index for a peak value 4
    print(
        f"{find_peak_index_v2([1,2,3,4,5,6,7,2,0])=}"
    )  # should return 6 index for a peak value 7
