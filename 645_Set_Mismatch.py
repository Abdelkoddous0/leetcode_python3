class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        duplicate = -1
        missing = -1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1

        if missing == -1 and nums[-1] != len(nums):
            missing = len(nums)

        if missing == -1:
            missing = 1

        return [duplicate, missing]
nums1 = [1, 2, 2, 4]
nums2 = [1, 1]

solution = Solution()
result1 = solution.findErrorNums(nums1)
result2 = solution.findErrorNums(nums2)

print("Test 1:", result1)  # Output should be [2, 3]
print("Test 2:", result2)  # Output should be [1, 2]

