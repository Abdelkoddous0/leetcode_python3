class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                current_substring = s[start:end]
                if is_palindrome(current_substring):
                    path.append(current_substring)
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
sol = Solution()
input_str1 = "aab"
print("Input:", input_str1)
print("Output:", sol.partition(input_str1))

input_str2 = "a"
print("Input:", input_str2)
print("Output:", sol.partition(input_str2))
