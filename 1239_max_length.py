class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s: str) -> bool:
            return len(s) == len(set(s))

        def backtrack(start: int, current: str) -> None:
            nonlocal max_length

            max_length = max(max_length, len(current))

            for i in range(start, len(arr)):
                if is_unique(current + arr[i]):
                    backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length


# Example usage:
arr1 = ["un", "iq", "ue"]
arr2 = ["cha", "r", "act", "ers"]
arr3 = ["abcdefghijklmnopqrstuvwxyz"]

solution = Solution()
print(solution.maxLength(arr1))  # Output: 4
print(solution.maxLength(arr2))  # Output: 6
print(solution.maxLength(arr3))  # Output: 26

