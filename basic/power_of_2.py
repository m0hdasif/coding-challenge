# https://leetcode.com/problems/power-of-two/submissions/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else (n & n - 1 == 0)


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(128))  # return True
    print(Solution().isPowerOfTwo(1))  # return True
    print(Solution().isPowerOfTwo(120))  # return False
