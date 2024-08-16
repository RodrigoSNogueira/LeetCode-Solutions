class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_mapping = {}

        for i, num in enumerate(nums): 
            solution = target - num
        
            if solution in num_mapping:
                return [num_mapping[solution], i]

            num_mapping[num] = i

        return []