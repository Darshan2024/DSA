from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # Dictionary to store {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num  # Find the required complement
            if complement in hash_map:
                return [hash_map[complement], i]  # Return indices of the pair
            hash_map[num] = i  # Store current number's index
        
        return []  # If no pair is found
