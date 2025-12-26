# 217. Contains Duplicate
"""
Problem: Check if an array contains duplicates.
If it does then return True, otherwise return False.


"""

class Solution:
    def containsDuplicate(self, nums: list[int])-> bool:
        return len(set(nums)) < len(nums)
    
# Example usage:
solution = Solution()
print("for the array [1, 2, 3, 1]:")
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print("for the array [1, 2, 3, 4]:")
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False