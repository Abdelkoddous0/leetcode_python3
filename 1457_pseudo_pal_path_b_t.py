class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path_count):
            if not node:
                return 0

            path_count[node.val] += 1

            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                odd_count = 0
                for count in path_count.values():
                    if count % 2 != 0:
                        odd_count += 1

                # If at most one digit has an odd count, the path is pseudo-palindromic
                if odd_count <= 1:
                    return 1
                else:
                    return 0

            # Recursively explore left and right subtrees
            left_count = dfs(node.left, path_count.copy())
            right_count = dfs(node.right, path_count.copy())

            return left_count + right_count

        return dfs(root, {i: 0 for i in range(1, 10)})

# Example usage:
solution = Solution()

root1 = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
print(solution.pseudoPalindromicPaths(root1))  # Output: 2

root2 = TreeNode(2, TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(3))), TreeNode(3)), None)
print(solution.pseudoPalindromicPaths(root2))  # Output: 1

root3 = TreeNode(9)
print(solution.pseudoPalindromicPaths(root3))  # Output: 1

