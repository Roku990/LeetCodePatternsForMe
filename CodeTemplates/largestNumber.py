# Problem: Find the largest number in the array

# Step 1: Understand the problem
"""
Input = [3,7,2,9,1]
Output = 9
Edge Cases: Empty Array, negative numbers
"""

# Step 2: Plan
"""
1. Start with the first number as the largest
2. Go through each number 
3. If the number is bigger than current largest, update largest
4. return largest number

"""

# Step 3: Implement

def find_largest(arr):
    if not arr:
        return None 
    
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

# Step 4: Test
print(find_largest([3,7,2,9,1]))  # Expected output: 9
print(find_largest([])) # Empty array
print(find_largest([-9,-12,-3,-7])) # Negative numbers

