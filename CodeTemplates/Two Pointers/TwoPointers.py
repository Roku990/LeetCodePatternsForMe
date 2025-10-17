# Two Pointer pattern
## EXPLAINATION:
#   WHAT IT IS: You use two variables left and right to move through a list or a string from different directions often the start 
#               and the end, to find a relationship between elements.
#   WHEN TO USE: 1. When you want to compare elements from both ends. 
#                2. Solve it in O(n) time
#                3. You are working with a sorted array or String.
#
#   PATTERN:
#   def fn(arr):
#       left = ans = 0
#       right = len(arr) - 1
#       while left < right:
#           #DO SOME LOGIC WITH LEFT AND RIGHT
#           if CONDITION:
#               left += 1
#           else:
#               right -= 1
#       return ans
#
#
#   EXAMPLE: PROBLEM 167. Two Sum II - Input Array Is Sorted
#       You are given a sorted array of integers "numbers", and a target integer "target".
#       Return the 1-based indicies of the two numbers such that they add up to target.
#       You must use exactly one pass O(n). No Hashmaps allowed.
#       INPUT: numbers = [2,7,11,15], target = 9, OUTPUT = [1,2] Because 2+7 =9
#

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum == target:
                #+1 because problem wants 1-based indicies
                return [left+1, right+1]
            
            elif currentSum < target:
                # Sum too small -> need a bigger number -> move left pointer right
                left += 1

            else:
                # Sum too big -> need a smaller number -> move right pointer left
                right -= 1

# ----------
# Test cases
solution = Solution()

#Example 1:
numbers = [2,7,11,15]
target = 9
print(f"The number List is {numbers}")
print(f"The target is {target}")
print("Output is: ",solution.twoSum(numbers,target)) # Output: [1,2]

#Example 2:
numbers = [1,2,3,4,6]
target = 6
print(f"The number List is {numbers}")
print(f"The target is {target}")
print("Output is: ",solution.twoSum(numbers,target)) # Output: [2,4]

#Example 3:
numbers = [1,3,4,5,6,8]
target = 11
print(f"The number List is {numbers}")
print(f"The target is {target}")
print("Output is: ",solution.twoSum(numbers,target)) # Output: [2,6]

