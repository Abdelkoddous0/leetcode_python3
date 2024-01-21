class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ''
        for x in s:
            if x.isalnum():  # Check if the character is alphanumeric
                ch += x.lower()
        return ch == ch[::-1]

# Test the provided testcase
solution = Solution()
result = solution.isPalindrome("0P")
print(result)

