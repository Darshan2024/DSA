class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hash_map = {}

        for i in range(len(nums)):
            if  nums[i] in hash_map and i - hash_map[nums[i]]<=k:
                return True

            hash_map[nums[i]] = i

        return False
