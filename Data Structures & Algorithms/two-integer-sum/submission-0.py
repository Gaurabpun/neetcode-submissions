class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        elements = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in elements:
                return [elements[diff], i]
                
            elements[num] = i

        return