class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = 0
        mod = 10**9 + 7

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k) % mod

            stack.append(i)

        # Handle remaining elements in the stack
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += arr[j] * (len(arr) - j) * (j - k) % mod

        return result % mod

# Example usage:
solution = Solution()
arr1 = [3, 1, 2, 4]
arr2 = [11, 81, 94, 43, 3]

print(solution.sumSubarrayMins(arr1))  # Output: 17
print(solution.sumSubarrayMins(arr2))  # Output: 444
