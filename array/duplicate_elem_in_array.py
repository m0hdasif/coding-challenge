# only 1 duplicate number from 0 to n-1
class Solution:
    # T(n)=O(n), S(n)=O(n)
    def find_duplicate_in_array(self, arr: list[int]) -> int:
        new_array = [None] * len(arr)
        for elem in arr:
            if new_array[elem]:
                return elem
            new_array[elem] = elem

        return None

    # xor twice cancels the element and return 0
    # T(n)=O(n), S(n)=O(1)
    def find_duplicate_in_array_by_xor(self, arr: list[int]) -> int:
        ans = 0
        for elem in arr:
            ans ^= elem

        for index, _ in enumerate(arr):
            ans ^= index

        return ans


if __name__ == "__main__":
    print(Solution().find_duplicate_in_array([1, 2, 4, 4, 3]))
    print(Solution().find_duplicate_in_array_by_xor([1, 2, 4, 3, 4, 5]))
