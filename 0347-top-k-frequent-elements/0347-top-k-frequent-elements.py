# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         freq = {}

#         for i in range len(nums):
#             if nums[i] in freq:
#                 freq[nums[i]] += 1
#                 continue

#             freq[nums[i]] = 1

#         freq_list = tuple(freq)

#         heapq.heapify(freq_list[1])

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count the frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Min-heap to keep the top k elements
        min_heap = []

        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))  # Push (frequency, number)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove the least frequent element

        # Extract top k frequent elements
        return [num for count, num in min_heap]
