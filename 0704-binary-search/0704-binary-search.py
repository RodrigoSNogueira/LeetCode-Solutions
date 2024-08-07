class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowest = 0 
        highest = len(nums) - 1

        while lowest <= highest:
            middle = (highest + lowest) // 2
            middle_value = nums[middle]

            if middle_value == target:
                return middle

            if middle_value > target:
                highest = middle - 1

            else: 
                lowest = middle + 1
                
        return -1